from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def product_all(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, "catalogue/index.html", {"products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "catalogue/single_product.html", {"product": product})


def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(name=slug).get_descendants(include_self=True))
    return render(request, "catalogue/category.html", {"category": category, "products": products})


def set_theme(request):
    theme = request.POST.get('theme', 'light')
    request.session['theme'] = theme
    request.session.modified = True
    return JsonResponse({'status': 'ok'})
