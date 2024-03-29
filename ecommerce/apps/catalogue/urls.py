from django.urls import path

from . import views

app_name = "catalogue"

urlpatterns = [
    path("", views.product_all, name="catalogue_home"),
    path("<slug:slug>", views.product_detail, name="product_detail"),
    path("shop/<slug:slug>/", views.category_list, name="category_list"),
    path("set_theme/", views.set_theme, name="set_theme"),
]
