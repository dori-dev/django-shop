from django.shortcuts import render
from django.views import View

from product import models


class Index(View):
    def get(self, request):
        products = models.Product.objects.filter(
            available=True,
        )
        categories = models.Category.objects.values('name', 'slug')
        context = {
            'products': products,
            'categories': categories,
        }
        return render(request, 'home/index.html', context)
