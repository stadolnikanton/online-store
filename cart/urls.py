from django.urls import path

from cart.views import CartView, OrderView


urlpatterns = [
    path("cart/", CartView.as_view(), name="cart"),
    path("order/", OrderView.as_view(), name="order"),
]
