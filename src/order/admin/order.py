from django.contrib import admin
from order.admin.item import OrderItemInline


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'paid',
        'total_price',
        'total_quantity',
        'updated',
    ]
    list_filter = [
        'paid',
    ]
    search_fields = [
        'user__username',
    ]
    inlines = [
        OrderItemInline,
    ]

    def total_price(self, obj):
        return f"{obj.get_total_price():,}"

    def total_quantity(self, obj):
        return f"{obj.get_total_quantity():,}"
