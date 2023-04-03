from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from order import models
from product.models import Product
from cart.cart import Cart


class CreateOrderView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        order = models.Order.objects.create(
            user=request.user,
        )
        for item in cart:
            try:
                product = Product.objects.get(
                    slug=item['slug']
                )
            except Product.DoesNotExist:
                print(
                    f"Product {item['product']} with "
                    f"slug {item['slug']} does not exists."
                )
                continue
            models.OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item['quantity'],
            )
        cart.clear()
        return redirect('order:detail', pk=order.pk)
