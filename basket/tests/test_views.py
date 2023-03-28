from django.test import TestCase
from django.urls import reverse

from account.models import UserBase
from store.models import Category, Product


class TestBasketView(TestCase):

    def setUp(self) -> None:
        UserBase.objects.create(email="admin@admin.com")
        Category.objects.create(name="django", slug="django")
        Product.objects.create(category_id=1, title="Django 1", created_by_id=1,
                               slug="django-1", price="100.00", image="django-1")
        Product.objects.create(category_id=1, title="Django 2", created_by_id=1,
                               slug="django-1", price="100.00", image="django-1")
        Product.objects.create(category_id=1, title="Django 3", created_by_id=1,
                               slug="django-1", price="100.00", image="django-1")
        self.client.post(
            reverse("basket:basket_add"), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True
        )
        self.client.post(
            reverse("basket:basket_add"), {"productid": 2, "productqty": 2, "action": "post"}, xhr=True
        )

    def test_home_url(self):
        """Test home page response status."""
        response = self.client.get(reverse("basket:basket_summary"))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        """Test adding items to the basket."""
        response = self.client.post(
            reverse("basket:basket_add"), {"productid": 3, "productqty": 1, "action": "post"}, xhr=True
        )
        self.assertEqual(response.json(), {"qty": 4})
        response = self.client.post(
            reverse("basket:basket_add"), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True
        )
        self.assertEqual(response.json(), {"qty": 3})

    def test_basket_delete(self):
        """Test removing items from the basket."""
        response = self.client.post(
            reverse("basket:basket_delete"), {"productid": 2, "action": "post"}, xhr=True
        )
        self.assertEqual(response.json(), {"qty": 1, "subtotal": "100.00"})

    def test_basket_update(self):
        """Test updating items in the basket."""
        response = self.client.post(
            reverse("basket:basket_update"), {"productid": 1, "productqty": 2, "action": "post"}, xhr=True
        )
        self.assertEqual(response.json(), {"qty": 4, "subtotal": "400.00"})
