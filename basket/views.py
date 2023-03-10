from django.shortcuts import render


def basket_summary(request):
    return render(request, "store/basket/summary.html")
