from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login, logout

from users.forms import UserRegisterForm
from api.views import send_registration_email


class Register(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "registration/register.html", {"form": form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            send_registration_email(user)
            login(
                request,
                user,
                backend="django.contrib.auth.backends.ModelBackend",
            )
            return redirect(to="/")
        else:
            print("Что-то не так!")

        return render(request, "registration/register.html", {"form": form})


class Logout(View):
    def post(self, request):
        print(request)
        logout(request)
        return redirect(to="/")


class Account(View):
    def get(self, request):
        return render(request, "user/account.html")
