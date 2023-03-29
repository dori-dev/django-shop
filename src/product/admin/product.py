from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'category',
        'price',
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
