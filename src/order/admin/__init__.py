from django.contrib import admin

from order import models
from order.admin import order, coupon

admin.site.register(models.Order, order.OrderAdmin)
admin.site.register(models.Coupon, coupon.CouponAdmin)
