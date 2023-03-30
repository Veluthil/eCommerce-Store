from django.urls import path

from . import views

app_name = "payment"

urlpatterns = [
    path("", views.basket_view, name="basket"),
    path("orderplaced/", views.order_placed, name="order_placed"),
    path("webhook/", views.stripe_webhook),
    path("error/", views.Error.as_view(), name="error"),
]
