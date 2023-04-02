from django.shortcuts import render
from django.views import View

from cart.cart import Cart


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        context = {
            'cart': cart,
        }
        return render(request, 'cart/detail.html', context)
