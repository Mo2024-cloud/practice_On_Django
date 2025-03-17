from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User  # Link form to User model
        fields = ["username", "email", "password"]  # Fields to display

    def clean(self):
        # Hold Dictionary That Hold User Data ["username", "email", "password"] with this Inputs After Django Validates THis Inputs
        cleaned_data = super().clean()
        password = cleaned_data.get("password")  # hold password From USer
        # hold confirm_password From USer
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("The Password is not Valid")

        return cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
