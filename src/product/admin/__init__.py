from django.contrib import admin

from product import models
from product.admin import category, product

admin.site.register(models.Category, category.CategoryAdmin)
admin.site.register(models.Product, product.ProductAdmin)
