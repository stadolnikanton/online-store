from django.contrib import admin
from django.urls import include, path

from shop.urls import urlpatterns as shop_patterns

from shop.views import IndexView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("admin/", admin.site.urls),
    path("", include(shop_patterns)),
    ]
