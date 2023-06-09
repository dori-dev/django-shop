from django.shortcuts import render, get_object_or_404
from django.views import View

from product import models
from cart.forms import CartAddForm


class ProductDetail(View):
    def get(self, request, slug):
        product = get_object_or_404(
            models.Product,
            slug=slug,
        )
        context = {
            'product': product,
            'form': CartAddForm(),
        }
        return render(request, 'product/detail.html', context)
