import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from basket.basket import Basket
from core.settings import SECRET_KEY_STRIPE
from orders.views import payment_confirmation

import stripe


@login_required()
def basket_view(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace(".", "")
    total = int(total)

    stripe.api_key = SECRET_KEY_STRIPE
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency="usd",
        metadata={"userid": request.user.id}
    )
    return render(request, "payment/payment_start.html", {"client_secret": intent.client_secret})


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the event
    if event.type == "payment_intent.succeeded":
        payment_confirmation(event.data.object.client_secret)
    else:
        print(f"Unhandled event type {event.type}")

    return HttpResponse(status=200)


def order_placed(request):
    basket = Basket(request)
    subject = "Order has been placed successfully."
    message = "We confirm that your order has been placed.\n " \
              "Thank you for shopping with us!\n" \
              "Dokushou Vernissage Team"
    request.user.email_user(subject=subject, message=message)
    basket.clear()
    return render(request, "payment/orderplaced.html")
