from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from account.models.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    phone = models.CharField(
        max_length=11,
        unique=True,
    )
    full_name = models.CharField(
        max_length=64,
        blank=False,
        null=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_admin = models.BooleanField(
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = [
        'email',
        'full_name',
    ]

    def __str__(self) -> str:
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
