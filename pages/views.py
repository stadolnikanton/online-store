from django.shortcuts import render
from django.views import View

from shop.models import Product, ProductType 

class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {"products": products}
        return render(request, "pages/index.html", context) 


class AboutView(View):
    def get(self, request):
        return render(request, "pages/about.html")
