from django.shortcuts import render, get_object_or_404
from django.views import View

from product import models


class CategoryView(View):
    def get(self, request, slug):
        category = get_object_or_404(
            models.Category,
            slug=slug,
        )
        categories = models.Category.objects.values('name', 'slug')
        context = {
            'products': category.products.filter(available=True),
            'categories': categories,
            'current_category': category.slug,
        }
        return render(request, 'home/index.html', context)
