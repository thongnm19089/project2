from .cart import Cart

#create context processor so our cart can work on all page on site
def cart(request):
    #Return the default data from our Cart
    return {'cart': Cart(request)}