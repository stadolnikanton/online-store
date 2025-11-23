from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from api.views import RegisterAPIView, LogoutAPIView, ProductListAPIView, ProductDetailAPIView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_paar'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', RegisterAPIView.as_view(), name='api_register'),
    path('logout/', LogoutAPIView.as_view(), name='api_logout'),
    

    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
]
