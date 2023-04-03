from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Coupon(models.Model):
    code = models.CharField(
        max_length=64,
        unique=True,
    )
    allowed_for = models.ManyToManyField(
        UserModel,
        related_name='coupons',
    )
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100),
        ],
    )
    active = models.BooleanField(
        default=True,
    )
    times = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs) -> None:
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.code
