from django.db import models


class OrderItem(models.Model):
    order = models.ForeignKey(
        'order.Order',
        on_delete=models.CASCADE,
        related_name='items',
    )
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(
        default=1,
    )

    def __str__(self) -> str:
        return f'{self.product.name} - order {self.pk}'

    def get_cost(self):
        return self.quantity * self.product.price
