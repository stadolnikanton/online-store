from django.urls import include, path

from users.views import Register, Logout, Account

urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("logout/", Logout.as_view(), name="logout"),
    path("account/", Account.as_view(), name="account"),
    path("", include("django.contrib.auth.urls")),
    path("", include("social_django.urls", namespace="social")),
]
