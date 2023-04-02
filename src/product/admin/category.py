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
        'parent__name',
    ]
    prepopulated_fields = {
        'slug': [
            'name',
        ]
    }
