from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile


class UserRegtrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # Link form to UserProfile model
        fields = ["name", "email", "age"]  # Fields to display


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


# class NumberSortForm(forms.Form):
#     numbers = forms.CharField(widget=forms.Textarea,
#                               help_text="Enter numbers separated by commas")
