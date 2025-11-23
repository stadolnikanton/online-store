from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from shop.urls import urlpatterns as shop_patterns
from pages.urls import urlpatterns as pages_patterns
from users.urls import urlpatterns as users_patterns
from cart.urls import urlpatterns as cart_patterns


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include(pages_patterns)),
    path("shop/", include(shop_patterns)),
    path("user/", include(users_patterns)),
    path("cart/", include(cart_patterns)),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
