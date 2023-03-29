from store.models import Product

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
        """Get the total price of the items in the basket."""
        return sum(Decimal(item["price"]) * item["qty"] for item in self.basket.values())

    def get_total_price(self):
        """Get the total price of the items in the basket including the shipping payment."""
        subtotal = sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())
        if subtotal == 0:
            shipping = Decimal(0.00)
        else:
            shipping = Decimal(8.50)
        total = subtotal + Decimal(shipping)
        return total

    def add(self, product, product_qty):
        """Add and update the dashboard's basket session data."""
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]["qty"] = product_qty
        else:
            self.basket[product_id] = {"price": str(product.price), "qty": int(product_qty)}
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
        self.save_session()

    def save_session(self):
        """Save the modified session data."""
        self.session.modified = True


"""
MIT License
Copyright (c) 2019 Packt
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""