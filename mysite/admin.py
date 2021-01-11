from django.contrib import admin
from .models import Customer,Store, Order, Product
# Register your models here.

# admin.site.register(Customer)
# admin.site.register(Store)
# admin.site.register(Order)
# admin.site.register(Product)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

