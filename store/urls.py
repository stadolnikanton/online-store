from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from api.urls import urlpatterns as api_patternts
from cart.urls import urlpatterns as cart_patterns
from pages.urls import urlpatterns as pages_patterns
from shop.urls import urlpatterns as shop_patterns
from users.urls import urlpatterns as users_patterns

schema_view = get_schema_view(
    openapi.Info(
        title="My API", default_version="v1", description="some desc"
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(pages_patterns)),
    path("shop/", include(shop_patterns)),
    path("user/", include(users_patterns)),
    path("cart/", include(cart_patterns)),
    path("api/", include(api_patternts)),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

    urlpatterns += [
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc/",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
        path(
            r"^swagger(?P<format>\.json|\.yaml)$",
            schema_view.with_ui(cache_timeout=0),
            name="schema-json",
        ),
    ]
