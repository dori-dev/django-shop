from django.shortcuts import redirect, get_object_or_404
from django.views import View

from product.models import Product
from cart.cart import Cart


class CarRemoveView(View):
    def get(self, request, slug):
        product = get_object_or_404(
            Product,
            slug=slug,
        )
        cart = Cart(request)
        cart.remove(product)
        return redirect('cart:detail')
