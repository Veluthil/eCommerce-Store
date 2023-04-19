from ecommerce.apps.checkout.models import DeliveryOptions
from ecommerce.apps.catalogue.models import Product

from django.conf import settings

from decimal import Decimal


class Basket:
    """A base Basket class that provides some default behaviors that can be inherited or overridden, as necessary."""

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if settings.BASKET_SESSION_ID not in request.session:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def __iter__(self):
        """Collect the product_id in the session data to query the database and return products."""
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()
        for product in products:
            basket[str(product.id)]["product"] = product
        for item in basket.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def __len__(self):
        """Get the basket data and count the quantity of items."""
        return sum(item["qty"] for item in self.basket.values())

    def get_subtotal(self):
        """Get the total price of the items in the basket."""
        return sum(Decimal(item["price"]) * item["qty"] for item in self.basket.values())

    def basket_update_delivery(self, delivery_price=0):
        """Add price of the chosen delivery to the total price of items in the basket."""
        subtotal = sum(Decimal(item["price"]) * item["qty"] for item in self.basket.values())
        total = subtotal + Decimal(delivery_price)
        return total

    def get_delivery_price(self):
        """Check user's session for previously chosen shipping method."""
        new_price = 0.00
        if "purchase" in self.session:
            new_price = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_price
        return new_price

    def get_delivery_option(self):
        """Check user's session for previously chosen shipping method."""
        new_delivery_option = ""
        if "purchase" in self.session:
            new_delivery_option = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_name
        return new_delivery_option

    def get_total_price(self):
        """Get the total price of the items in the basket including the shipping payment."""
        subtotal = sum(Decimal(item["price"]) * item["qty"] for item in self.basket.values())
        new_price = 0.00
        if "purchase" in self.session:
            new_price = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_price
        total = subtotal + Decimal(new_price)
        return total

    def add(self, product, product_qty):
        """Add and update the dashboard's basket session data."""
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]["qty"] = product_qty
        else:
            self.basket[product_id] = {"price": str(product.regular_price), "qty": int(product_qty)}
        self.save_session()

    def delete(self, product):
        """Delete item from session data by its ID."""
        product_id = str(product)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save_session()

    def update(self, product, qty):
        """Update item in the session by its ID and selected quantity."""
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]["qty"] = qty
        self.save_session()

    def clear(self):
        """Remove basket from session."""
        del self.session[settings.BASKET_SESSION_ID]
        del self.session["address"]
        del self.session["purchase"]
        self.save_session()

    def save_session(self):
        """Save the modified session data."""
        self.session.modified = True
