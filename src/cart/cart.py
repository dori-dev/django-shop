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
        slug = product.slug
        if slug not in self.cart:
            self.cart[slug] = {
                'slug': slug,
                'product': product.name,
                'quantity': quantity,
                'price': product.price,
            }
        else:
            self.cart[slug]['quantity'] = quantity
        item = self.cart[slug]
        item['total_price'] = item['price'] * quantity
        self.save()

    def remove(self, product: Product):
        slug = product.slug
        if slug in self.cart:
            del self.cart[slug]
            self.save()

    def save(self):
        self.session.modified = True

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()
