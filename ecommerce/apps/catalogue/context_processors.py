from .models import Category


def all_categories(request):
    return {"categories": Category.objects.filter(level=0)}
