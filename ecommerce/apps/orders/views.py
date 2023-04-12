from django.http.response import JsonResponse

from ecommerce.apps.basket.basket import Basket
from .models import Order, OrderItem


def add(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        user_id = request.user.id
        full_name = request.user.first_name + " " + request.user.surname
        address_1 = request.user.address_1
        address_2 = request.user.address_2
        city = request.user.city
        order_key = request.POST.get("order_key")
        baskettotal = basket.get_total_price()

        # check if the order already exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(user_id=user_id, full_name=full_name, address_1=address_1,
                                         address_2=address_2, city=city, total_paid=baskettotal, order_key=order_key)
            order_id = order.pk
            for item in basket:
                OrderItem.objects.create(order_id=order_id, product=item["product"], price=item["price"],
                                         quantity=item["qty"])

        response = JsonResponse({"success": "Successfully returned."})
        return response


def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders
