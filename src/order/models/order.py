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
    discount = models.IntegerField(
        blank=True,
        null=True,
        default=0,
    )

    class Meta:
        ordering = (
            'paid',
            '-updated',
        )

    def __str__(self):
        return f'{self.user} - {self.pk}'

    def get_total_price(self):
        total_price = self.get_real_total_price()
        if self.discount:
            total_price = int(total_price * (1 - self.discount/100))
        return total_price

    def get_real_total_price(self):
        return sum(
            item.get_cost()
            for item in self.items.all()
        )

    def get_total_quantity(self):
        return sum(
            item.quantity
            for item in self.items.all()
        )
