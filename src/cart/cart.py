from django.core.handlers.wsgi import WSGIRequest
from product.models import Product

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request: WSGIRequest):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if cart is None:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        for item in self.cart.values():
            yield item

    def __len__(self):
        return sum(
            item['quantity']
            for item in self.cart.values()
        )

    def price(self):
        return sum(
            item['total_price']
            for item in self.cart.values()
        )

    def add(self, product: Product, quantity):
        product_slug = product.slug
        if product_slug not in self.cart:
            self.cart[product_slug] = {
                'product': product.name,
                'quantity': quantity,
                'price': product.price,
            }
        else:
            self.cart[product_slug]['quantity'] = quantity
        item = self.cart[product_slug]
        item['total_price'] = item['price'] * quantity
        self.save()

    def save(self):
        self.session.modified = True
