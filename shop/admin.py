from django.contrib import admin
from shop.models import Product, ProductType


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "count", "product_types", "image")
    list_filter = ("name", "product_types")


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ("title",)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
