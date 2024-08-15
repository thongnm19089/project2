from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(ShippingAddress)
admin.site.register(Category)
admin.site.register(Suppiler)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Order)
admin.site.register(OrderItem)