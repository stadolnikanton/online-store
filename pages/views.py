from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from shop.models import Product, ProductType, Cart, CartItem

class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        product_types = ProductType.objects.all()

        product_types_id = request.GET.get('product_types_id')
        query = request.GET.get('q')

        if product_types_id:
            try:
                selected_type = ProductType.objects.get(id=product_types_id)
                products = products.filter(product_types=selected_type)
            except ProductType.DoesNotExist:
                selected_type = None
        else:
            selected_type = None

        if query:
            products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

        paginator = Paginator(products, 8)
        
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)


        if request.user.is_authenticated:
            try:
                cart = Cart.objects.get(user=request.user)
                cart_items = CartItem.objects.filter(cart=cart)
                cart_items_count = cart_items.count()
            except Cart.DoesNotExist:
                pass

        context = {
            "products": products,
            "product_types": product_types,
            "selected_type": selected_type,
            "page_obj": page_obj,
            "query": query,
            "cart_items_count": cart_items_count,
            "cart_items": cart_items,
            "cart": cart,
        }
        return render(request, "pages/index.html", context) 


class AboutView(View):
    def get(self, request):
        return render(request, "pages/about.html")
