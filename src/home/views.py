from django.shortcuts import render
from django.views import View

from product import models


class Index(View):
    def get(self, request):
        products = models.Product.objects.filter(
            available=True,
        )
        context = {
            'products': products,
        }
        return render(request, 'home/index.html', context)
