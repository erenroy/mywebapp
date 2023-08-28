from django.contrib import admin
from .models import Post
from .models import Contact
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced
)

# @admin.register(Customer)
#class CustomerModelAdmin(admin.ModelAdmin):
#    list_display = ['id', 'user' , 'name' , 'locality' , 'city' , 'zipcode' , 'state']

admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Post)

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'selling_price' ,  'discounted_price' , 'brand' , 'category' , 'product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user' , 'customer' , 'product' , 'quantity' , 'ordered_date' , 'status']
