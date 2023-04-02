from django.contrib import admin

from order import models
from order.admin import order

admin.site.register(models.Order, order.OrderAdmin)
