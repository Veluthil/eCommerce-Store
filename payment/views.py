from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from basket.basket import Basket

import stripe


@login_required()
def basket_view(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace(".", "")
    total = int(total)

    stripe.api_key = "INSERT YOUR STRIPE SECRET KEY HERE"
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency="usd",
        metadata={"userid": request.user.id}
    )
    return render(request, "payment/payment_start.html", {"client_secret": intent.client_secret})


