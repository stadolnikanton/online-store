from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from shop.models import Product

class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        paginator = Paginator(products, 8)
        
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
                "products": products, 
                "page_obj": page_obj
                }
        return render(request, "pages/index.html", context) 


class AboutView(View):
    def get(self, request):
        return render(request, "pages/about.html")
