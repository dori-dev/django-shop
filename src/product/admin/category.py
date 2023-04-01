from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'parent',
        'is_child',
        'slug',
    ]
    search_fields = [
        'name',
    ]
    prepopulated_fields = {
        'slug': [
            'name',
        ]
    }
