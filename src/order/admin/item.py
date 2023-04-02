from django.contrib import admin
from order.models import OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = [
        'product',
    ]
