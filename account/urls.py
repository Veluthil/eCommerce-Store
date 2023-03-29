from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from . import views
from .forms import UserLoginForm, PwdResetForm, PwdResetConfirmForm

app_name = "account"

urlpatterns = [
    path("register/",
         views.account_register, name="register"),
    path("activate/<slug:uidb64>/<slug:token>",
         views.account_activate, name="activate"),
    path("dashboard/",
         views.dashboard, name="dashboard"),
    path("login/",
         auth_views.LoginView.as_view(template_name="account/login.html", form_class=UserLoginForm),
         name="login"),
    path("logout/",
         auth_views.LogoutView.as_view(next_page="/account/login/"), name="logout"),
    path("profile/edit/",
         views.edit_details, name="edit_details"),
    path("profile/delete_user/",
         views.delete_user, name="delete_user"),
    path("profile/confirm_delete/",
         TemplateView.as_view(template_name="account/dashboard/confirm_delete.html"), name="delete_confirmation"),
    path("password_reset/",
         auth_views.PasswordResetView.as_view(template_name="account/password_reset/password_reset_form.html",
                                              success_url="password_reset_email_confirm",
                                              email_template_name="account/password_reset/password_reset_email.html",
                                              form_class=PwdResetForm), name="pwdreset"),
    path("password_reset_confirm/<uidb64>/<token>",
         auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset/password_reset_confirm.html",
                                                     success_url="/account/password_reset_complete/",
                                                     form_class=PwdResetConfirmForm), name="password_reset_confirm"),
    path("password_reset/password_reset_email_confirm/",
         TemplateView.as_view(template_name="account/password_reset/reset_status.html"), name="password_reset_done"),
    path("password_reset_complete/",
         TemplateView.as_view(template_name="account/password_reset/reset_status.html"), name="password_reset_complete"),
]
