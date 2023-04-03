from django.contrib import admin


class CouponAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'valid_from',
        'valid_to',
        'discount',
        'active',
        'times',
    ]
    list_filter = [
        'active',
    ]
    search_fields = [
        'code',
        'discount',
    ]
