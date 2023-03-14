from store.models import Product

from decimal import Decimal


class Basket:
    """A base Basket class that provides some default behaviors that can be inherited or overridden, as necessary."""

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get("session_key")
        if "session_key" not in request.session:
            basket = self.session["session_key"] = {}
        self.basket = basket

    def add(self, product, product_qty):
        """Add and update the user's basket session data."""
        product_id = product.id
        if product_id not in self.basket:
            self.basket[product_id] = {"price": str(product.price), "qty": int(product_qty)}
        self.session.modified = True

    def __iter__(self):
        """Collect the product_id in the session data to query the database and return products."""
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
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
        """Get the total price of items in the basket."""
        return sum(Decimal(item["price"]) * item["qty"] for item in self.basket.values())
