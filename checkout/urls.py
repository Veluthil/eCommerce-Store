from django.urls import path

from . import views

app_name = "checkout"

urlpatterns = [
    path("delivery_choices/", views.delivery_choices, name="delivery_choices"),
    path("basket_update_delivery/", views.basket_update_delivery, name="basket_update_delivery"),
    # path("delivery_address/", views.delivery_address, name="delivery_address"),
    # path("payment_selection/", views.payment_selection, name="payment_selection"),
    # path("payment_complete/", views.payment_complete, name="payment_complete"),
    # path("payment_successful/", views.payment_successful, name="payment_successful"),
]
