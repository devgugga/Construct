from django.urls import path

from . import views

urlpatterns = [
    path("register_seller/", views.register_seller, name="register_seller"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
