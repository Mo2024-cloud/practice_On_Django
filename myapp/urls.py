from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create-user/", views.create_user, name="create_user"),
    path("update-user/", views.update_user, name="update_user"),
    path("delete-user/", views.delete_user, name="delete_user"),
    path("register/", views.register_user, name="register"),
    path("success/", views.success, name="success"),
    path("login/", views.login_user, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_user, name="logout"),

]
