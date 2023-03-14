

class Basket:
    """A base Basket class that provides some default behaviors that can be inherited or overrided, as necessary."""

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

    def __len__(self):
        """Get the basket data and count the quantity of items."""
        return sum(item["qty"] for item in self.basket.values())
