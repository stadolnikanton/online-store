from django.shortcuts import render, get_object_or_404
from django.views import View

from shop.models import Product


class ProductDetail(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        context = {
            "product": product,
        }
        return render(request, "product/product_detail.html", context)
