from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from basket.basket import Basket
from store.models import Product


def basket_summary(request):
    basket = Basket(request)
    return render(request, "basket/summary.html", {"basket": basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productid"))
        product_qty = int(request.POST.get("productqty"))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, product_qty=product_qty)
        basket_qty = basket.__len__()
        response = JsonResponse({"qty": basket_qty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productid"))
        basket.delete(product=product_id)

        basket_qty = basket.__len__()
        basket_total = basket.get_subtotal()
        response = JsonResponse({"qty": basket_qty, "subtotal": basket_total})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productid"))
        product_qty = int(request.POST.get("productqty"))
        basket.update(product=product_id, qty=product_qty)

        basket_qty = basket.__len__()
        basket_total = basket.get_subtotal()
        response = JsonResponse({"qty": basket_qty, "subtotal": basket_total})
        return response
