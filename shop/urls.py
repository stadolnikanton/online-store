from django.urls import path

from shop.views import Product

urlpatterns= [
        path('', Product.as_view(), name="product"),
]
