from django.shortcuts import redirect, get_object_or_404
from django.views import View

from product.models import Product


class CartAddView(View):
    def post(self, request, slug):
        product = get_object_or_404(
            Product,
            slug=slug,
        )
        return redirect(product.get_absolute_url())
