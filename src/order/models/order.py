from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='orders',
    )
    paid = models.BooleanField(
        default=False,
    )
    total_price = models.PositiveBigIntegerField(
        null=True,
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = (
            'paid',
            '-updated',
        )

    def __str__(self):
        return f'{self.user} - {self.pk}'

    def get_total_price(self):
        return sum(
            item.get_cost()
            for item in self.items.all()
        )

    def get_total_quantity(self):
        return sum(
            item.quantity
            for item in self.items.all()
        )
