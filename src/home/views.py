from django.shortcuts import render
from django.views import View
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from product import models


@method_decorator(cache_page(60 * 15), name='dispatch')
class Index(View):
    def get(self, request):
        products = models.Product.objects.filter(
            available=True,
        )
        categories = models.Category.objects.filter(is_child=False)
        context = {
            'products': products,
            'categories': categories,
        }
        return render(request, 'home/index.html', context)
