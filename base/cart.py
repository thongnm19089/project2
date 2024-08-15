from .models import Product, User
from django.contrib import messages
class Cart():
    def __init__(self, request):
        self.request = request
        self.session = request.session

        #Get the current session key if exists
        cart = self.session.get('session_key')
        
        #If the user is new, no session, create a new one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #make sure cart is available on all pages of site
        self.cart = cart
    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)
        #Logic
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price_sell)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True
        #Deal with logged in user
        if self.request.user.is_authenticated:
            #Get the current user profile
            current_user = User.objects.filter(id=self.request.user.id)
            #Change quatation mark form single to double for later in order to convert form string to dict using json
            #{'3':1,'4':2} -> {"3":1,"4":2}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            #save the carty to user model
            current_user.update(old_cart=str(carty))
    def add(self, product, quantity):
        product_old_qty = str(product.quantity)
        product_id = str(product.id)
        product_qty = str(quantity)
        #Logic
        if product_id in self.cart:
            if self.cart[product_id] + int(product_qty) > int(product_old_qty):
                self.cart[product_id] = int(product_old_qty)
            else:
                self.cart[product_id] += int(product_qty)
        else:
            #self.cart[product_id] = {'price': str(product.price_sell)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True
        #Deal with logged in user
        if self.request.user.is_authenticated:
            #Get the current user profile
            current_user = User.objects.filter(id=self.request.user.id)
            #Change quatation mark form single to double for later in order to convert form string to dict using json
            #{'3':1,'4':2} -> {"3":1,"4":2}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            #save the carty to user model
            current_user.update(old_cart=str(carty))
    def __len__(self):
        return len(self.cart)
    #Get product
    def get_prods(self):
        #Get ids from cart
        product_ids = self.cart.keys()
        #Use ids to lookup products in DB
        products = Product.objects.filter(id__in=product_ids) 
        #Return list of found products
        return products
    def get_quants(self):
        quantites = self.cart
        return quantites
    def update(self,product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        #Get cart
        ourcart = self.cart
        #Update cart, which is by now a dictionary {'4':2, '1':3}
        ourcart[product_id] = product_qty

        self.session.modified = True
        if self.request.user.is_authenticated:
            #Get the current user profile
            current_user = User.objects.filter(id=self.request.user.id)
            #Change quatation mark form single to double for later in order to convert form string to dict using json
            #{'3':1,'4':2} -> {"3":1,"4":2}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            #save the carty to user model
            current_user.update(old_cart=str(carty))
        thing = self.cart
        return thing
    def delete(self, product):
        product_id = str(product)
        #Delete from dictionary cart
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True
        if self.request.user.is_authenticated:
            #Get the current user profile
            current_user = User.objects.filter(id=self.request.user.id)
            #Change quatation mark form single to double for later in order to convert form string to dict using json
            #{'3':1,'4':2} -> {"3":1,"4":2}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            #save the carty to user model
            current_user.update(old_cart=str(carty))
    def clear_cart(self):
        print("Clearing cart...")
        self.cart = {}
        self.session.modified = True
        if self.request.user.is_authenticated:
            current_user = User.objects.filter(id=self.request.user.id)
            carty = str(self.cart)
            current_user.update(old_cart=str(carty))
    def cart_total(self):
        #Get product ids
        product_ids = self.cart.keys()
        #look up keys in Product model
        products = Product.objects.filter(id__in=product_ids)
        #Get quantities
        quantities = self.cart
        #start counting
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price_sell * value)
        return total
    def item_total(self):
        total_dict = {} 
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            product_id = str(product.id)
            quantity = self.cart.get(product_id, 0)
            if product.is_sale:
                total_price = product.sale_price * quantity
            else:
                total_price = product.price_sell * quantity
            total_dict[product_id] = total_price
        return total_dict
    
        
