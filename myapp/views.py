from termios import OPOST
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import UserProfile
from .forms import UserRegtrationForm, LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.


# Insert User
def home(request):
    context = {
        "name": "Mohamed",
        "age": 25,
        "hoppies": ["Coding", "Problem Solveing", "Django Legend"]
    }
    return render(request, "myapp/home.html", context)


# Create User
def create_user(request):
    user = UserProfile(name="Mohamed", email="mr@gmail.com", age=25)
    user.save()
    return HttpResponse("User Created Successfully")


# Update User
def update_user(request):
    user = UserProfile.objects.get(email="Mo@gmail.com")
    user.age = 26
    user.save()
    return HttpResponse("User Updated Successfully")


# Delete User
def delete_user(request):
    user = UserProfile.objects.get(email="Mo@gmail.com")
    user.delete()
    return HttpResponse("User Deleted Successfully")


# Register Function
def register_user(request):
    if request.method == "POST":
        form = UserRegtrationForm(request.POST)  # Get user input
        if form.is_valid():
            form.save()  # Save user to database
            return redirect("success")  # Redirect to success page

    else:
        form = UserRegtrationForm()  # Empty form for GET request

    return render(request, "myapp/register.html", {"form": form})


# Login Function
def login_user(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # Get the input from user using cleaned_data that get input using Dict. by Key And store in username
            username = form.cleaned_data["username"]
            # Get the input from user using cleaned_data that get input using Dict. by Key And store in password
            password = form.cleaned_data["password"]
            # Check if username that user enter === username that store in BataBase
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
    else:
        form = LoginForm()

    return render(request, "myapp/login.html", {"form": form})

# Success Page


def success(request):
    return render(request, "myapp/success.html")


@login_required
def dashboard(request):
    return render(request, "myapp/dashboard.html")


def logout_user(request):
    logout(request)
    return redirect("login")
