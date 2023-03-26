from django.urls import path

from . import views

app_name = "payment"

urlpatterns = [
    path("", views.basket_view, name="basket"),
]
