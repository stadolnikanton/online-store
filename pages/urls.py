from django.urls import path

from pages.views import IndexView, AboutView

urlpatterns = [
    path("", IndexView.as_view(), name="index_page"),
    path("about/", AboutView.as_view(), name="about_page"),
]
