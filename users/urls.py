from django.urls import include, path
from django.contrib.auth.views import LoginView

from users.views import Register, Logout

urlpatterns= [
#        path('login/', LoginView.as_view(template_name="user/login.html"), name='login'),
        path('register/', Register.as_view(), name='register'),
        path('logout/', Logout.as_view(), name='logout'),
        path('', include('django.contrib.auth.urls')),
]
