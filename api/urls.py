from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from api.views import (
    RegisterAPIView,
    LogoutAPIView,
    ProductDetailsAPIView,
    ProductListAPIView,
)
from api.views import (
    CartAPIView,
    CartAddItemAPIView,
    CartRemoveItemAPIView,
    CartUpdateItemAPIView,
)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_paar"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterAPIView.as_view(), name="api_register"),
    path("logout/", LogoutAPIView.as_view(), name="api_logout"),
    path("products/", ProductListAPIView.as_view(), name="products"),
    path("products/<int:pk>/", ProductDetailsAPIView.as_view(), name="product-detail"),
    path("cart/", CartAPIView.as_view(), name="cart-detail"),
    path("cart/add/", CartAddItemAPIView.as_view(), name="cart-add"),
    path(
        "cart/remove/<int:product_id>/",
        CartRemoveItemAPIView.as_view(),
        name="cart-remove",
    ),
    path(
        "cart/update/<int:product_id>/",
        CartUpdateItemAPIView.as_view(),
        name="cart-update",
    ),
]
