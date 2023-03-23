from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from . import views
from .forms import UserLoginForm

app_name = "account"

urlpatterns = [
    path("register/", views.account_register, name="register"),
    path("activate/<slug:uidb64>/<slug:token>", views.account_activate, name="activate"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/",
         auth_views.LoginView.as_view(template_name="account/registration/login.html", form_class=UserLoginForm),
         name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/account/login/"), name="logout"),
    path("profile/edit/", views.edit_details, name="edit_details"),
    path("profile/delete_user/", views.delete_user, name="delete_user"),
    path("profile/confirm_delete/", TemplateView.as_view(template_name="account/user/confirm_delete.html"),
         name="delete_confirmation"),
]
