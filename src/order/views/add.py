from django.shortcuts import redirect, get_object_or_404
from django.views import View

from product.models import Product
from order.cart import Cart
from order.forms import CartAddForm


class CartAddView(View):
    def post(self, request, slug):
        form = CartAddForm(request.POST)
        product = get_object_or_404(
            Product,
            slug=slug,
        )
        quantity = 1
        if form.is_valid():
            quantity = form.cleaned_data.get('quantity')
        cart = Cart(request)
        cart.add(product, quantity)
        return redirect('order:cart')
