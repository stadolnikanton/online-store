from django.contrib import admin
from django.urls import include, path

from shop.urls import urlpatterns as shop_patterns
from pages.urls import urlpatterns as pages_patterns
from users.urls import urlpatterns as users_patterns


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include(pages_patterns)),
    path("shop/", include(shop_patterns)),
    path("user/", include(users_patterns)),
    ]
