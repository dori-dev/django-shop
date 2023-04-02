from django.shortcuts import render, get_object_or_404
from django.views import View

from product import models


class CategoryView(View):
    def get(self, request, slug):
        category = get_object_or_404(
            models.Category,
            slug=slug,
        )
        categories = models.Category.objects.filter(is_child=False)
        current_category = category
        while current_category.is_child:
            current_category = current_category.parent
        context = {
            'products': category.products.filter(available=True),
            'categories': categories,
            'category_slug': current_category.slug,
        }
        return render(request, 'home/index.html', context)
