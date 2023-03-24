from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required()
def basket_view(request):
    return render(request, "payment/payment_start.html")
