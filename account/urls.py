from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path("register/", views.account_register, name="register"),
]
