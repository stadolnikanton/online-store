from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(
        label="Your name:",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your name",
            }
        ),
    )

    email = forms.CharField(
        label="Email adress:",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your email",
            }
        ),
    )

    password = forms.CharField(
        label="Password:",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter password",
            }
        ),
    )

    password2 = forms.CharField(
        label="Password confirm",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter password confirm",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
