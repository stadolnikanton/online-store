from django.urls import path
from shop.views import CartView, ProductDetail


urlpatterns= [
        path('<int:pk>/', ProductDetail.as_view(), name="product_detail"),
        path('cart/', CartView.as_view(), name='cart'),
]
