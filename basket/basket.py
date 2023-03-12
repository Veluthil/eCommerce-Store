

class Basket:
    """A base Basket class that provides some default behaviors that can be inherited or overrided, as necessary."""

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get("session_key")
        if "session_key" not in request.session:
            basket = self.session["session_key"] = {}
        self.basket = basket


