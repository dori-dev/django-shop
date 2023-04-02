from django.core.handlers.wsgi import WSGIRequest

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request: WSGIRequest):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if cart is None:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity):
        product_slug = product.slug
        if product_slug not in self.cart:
            self.cart[product_slug] = {
                'quantity': 0,
                'price': str(product.price),
            }
        self.cart[product_slug]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True
