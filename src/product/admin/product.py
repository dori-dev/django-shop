from django.contrib import admin
from django.utils.html import format_html


class ProductAdmin(admin.ModelAdmin):
    exclude = [
        'slug',
    ]
    list_display = [
        'name',
        'category',
        'price',
        'link',
        'available',
        'updated',
    ]
    list_filter = [
        'available',
        'updated',
    ]
    search_fields = [
        'name',
        'category',
        'description',
    ]

    def link(self, model):
        url = model.get_absolute_url()
        return format_html(
            f'<a target="_blank" href="{url}">Open</a>'
        )
