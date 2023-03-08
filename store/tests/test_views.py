# from unittest import skip
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.http import HttpRequest
from django.contrib.auth.models import User
from store.models import Category, Product
from store.views import all_products


class TestViewResponses(TestCase):

    def setUp(self) -> None:
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name="django", slug="django")
        User.objects.create(username="admin")
        Product.objects.create(category_id=1, title="Django 1", created_by_id=1,
                               slug="django-1", price="99.99", image="django-1")

    def test_url_allowed_hosts(self):
        """Tests allowed hosts."""
        response = self.c.get("/")
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """Tests product response status."""
        response = self.c.get(reverse("store:product_detail", args=["django-1"]))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """Tests category response status."""
        response = self.c.get(reverse("store:category_list", args=["django"]))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """Test homepage response status."""
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode("utf8")
        self.assertIn("<title>Home</title>", html)
        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get("/product/django-1")
        response = all_products(request)
        html = response.content.decode("utf8")
        self.assertIn("<title>Home</title>", html)
        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code, 200)
