from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
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
