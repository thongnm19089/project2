from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from django.db.models import Q, Sum
import re
from .models import *


def process_message(message):
    # deal with user message
    message = message.replace(".","").replace(",","").replace("?","").replace("!","").replace(";","").replace(":","")
    message = message
    stop_words = set(stopwords.words("english"))
    #seperate the message to each word
    words = word_tokenize(message)
    #remove the common stop words
    filtered_words = [word for word in words if word not in stop_words]

    lemmatizer = WordNetLemmatizer()
    stemmed_words = [lemmatizer.lemmatize(word) for word in filtered_words]
    processed_message = " ".join(stemmed_words)
    print(f"Processed Message: {processed_message}")
    return processed_message
def handle_greeting(message):
  informal_greetings_pattern = r"^\W*(hi+|hey+|hello+|\bh[ei]llo\b|\swatchya|sup|good morning|good afternoon|good evening|good night|hey there|howdy|what's up)\W*$"
  match = re.search(informal_greetings_pattern, message)
  if match:
      return "Hey! How can I assist you today? 😚"
  else:
      return None
def handle_product_search(message):
  products = Product.objects.filter(Q(name__icontains=message) | Q(suppiler__name__icontains=message))
  if products:
    response = f"Here are some results for '{message}':\n"
    for product in products:
      product_url = f"/product/{product.id}"
      response += f"- <a href='{product_url}'>{product.name}</a>\n"
    return response
  else:
    return None
def handle_sale_product(message):
  sale_pattern = r"\W*(sale|sales|on\s*sale|discount)\W*"
  suppilers = Suppiler.objects.all()
  suppiler_names = [suppiler.name.lower() for suppiler in suppilers]
  suppiler_pattern = r"\W*(" + "|".join(suppiler_names) + r")\W*"
  sale_match = re.search(sale_pattern, message.lower())
  suppiler_match = re.search(suppiler_pattern, message.lower())

  if sale_match:
      if suppiler_match:
        suppiler_name = suppiler_match.group(1)  #get the suppiler name from matched above
        sale_products = Product.objects.filter(
          is_sale=True, suppiler__name__icontains=suppiler_name
        )
        if sale_products:
          response = f"**Sale products from {suppiler_name}:**\n"
          for product in sale_products:
            product_url = f"/product/{product.id}"
            response += f"- <a href='{product_url}'>{product.name}</a>: ${product.sale_price}\n"
          return response
        else:
          return f"There are currently no sale products from {suppiler_name}."
      else:
        sale_products = Product.objects.filter(
           is_sale=True
        )
        if sale_products:
          response = f"**Sale products**\n"
          for product in sale_products:
            product_url = f"/product/{product.id}"
            response += f"- <a href='{product_url}'>{product.name}</a>: ${product.sale_price}\n"
          return response
        else:
          return f"There are currently no ongoing sales."
  else:
    return None
def handle_top_product(message):
  top_pattern = r"\W*(top|best|most\s*sale|great)\W*"
  top_match = re.search(top_pattern, message.lower())
  if top_match:
    suppilers = Suppiler.objects.all()
    suppiler_names = [suppiler.name.lower() for suppiler in suppilers ]
    suppiler_pattern = r"\W*(" + "|".join(suppiler_names) + r")\W*"
    suppiler_match = re.search(suppiler_pattern, message.lower())
    if suppiler_match:
      suppiler_name = suppiler_match.group(1)
      products = Product.objects.filter(suppiler__name__icontains=suppiler_name, orderitem__order__status=4)
      products = products.annotate(sales_count=Sum('orderitem__quantity', filter=Q(orderitem__order__status=4)))
      if products.count() > 0:
        products = products.order_by('-sales_count')[:5]
        response = f"The top selling products from {suppiler_name}:\n"
        for product in products:
          product_url = f"/product/{product.id}"
          response += f"- <a href='{product_url}'>{product.name}</a>\n"
        return response
      else:
        return "This brand has not sold anything yet"
    else:
      products = Product.objects.filter(orderitem__order__status=4)
      products = products.annotate(sales_count=Sum('orderitem__quantity'))
      if products.count() > 0:
        response = f"The top selling products\n"
        products = products.order_by('-sales_count')[:5]
        for product in products:
          product_url = f"/product/{product.id}"
          response += f"- <a href='{product_url}'>{product.name}</a>\n"
        return response
      else:
         return "Sorry, i have not sold anything yet 😅"
  else:
     return None
def handle_payment(message):
  payment_pattern = r"\W*(pay|payment|checkout|purchase)\W*"
  ship_pattern = r"\W*(ship|shipping)\W*"
  pay_match = re.search(payment_pattern, message.lower())
  ship_match = re.search(ship_pattern, message.lower())
  if pay_match:
      return "We only accept PayPal as a form of payment."
  elif ship_match:
      return "All of our orders come with free shipping. 😉"
  else:
      return None
def handle_shipping(message):
  ship_pattern = r"\W*(ship|shipping)\W*"
  ship_match = re.search(ship_pattern, message.lower())
  if ship_match:
    return "All of our orders come with free shipping. 😉"
  else:
    return None
def handle_help(message):
  if "help" in message:
    return "Here are some things I can do:\n" + \
           "- Help you find products\n" + \
           "- Answer your questions about our products and services\n" + \
           "- (**Future implementation**) Track your order status\n" + \
           "- (**Future implementation**) Provide customer support"
  return None
def handle_cant_understand(message):
    return "Sorry, im not able to understand that, pls try again 😵"
def get_response(message):
    processed_message = process_message(message)
    response = (
        handle_greeting(processed_message) or
        handle_product_search(processed_message) or
        handle_sale_product(processed_message) or
        handle_top_product(processed_message) or
        handle_payment(processed_message) or
        handle_shipping(processed_message) or
        handle_help(processed_message)
    )
    return response or handle_cant_understand(processed_message)
