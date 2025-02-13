from django.contrib import admin
from .models import Product,Order
# Register your models here.
admin.site.site_header = "E-Commerce Site"
admin.site.site_title = "Fancyy"
admin.site.index_title = "Manage Fancyy Shop Database"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_price', 'category')
    search_fields = ('title',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)