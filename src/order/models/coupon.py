from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from django.utils.timezone import now

UserModel = get_user_model()


class Coupon(models.Model):
    code = models.CharField(
        max_length=64,
        unique=True,
    )
    allowed_for = models.ManyToManyField(
        UserModel,
        blank=True,
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

    def __str__(self) -> str:
        return self.code

    @staticmethod
    def get(code, user):
        current_time = now()
        coupon_qs = Coupon.objects.filter(
            code__exact=code,
            valid_from__lte=current_time,
            valid_to__gte=current_time,
            active=True,
        )
        if not coupon_qs.exists():
            return None
        coupon = coupon_qs.first()
        if coupon.allowed_for.exists() and user not in coupon.allowed_for:
            return None
        if coupon.times is not None:
            coupon.times -= 1
            if coupon.times <= 0:
                coupon.active = False
            coupon.save()
        return coupon
