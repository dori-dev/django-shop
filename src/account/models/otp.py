from random import choices

from django.db import models


class OtpCode(models.Model):
    phone = models.CharField(
        max_length=11,
    )
    code = models.CharField(
        max_length=4,
        null=True,
        blank=True,
    )
    created = models.DateTimeField(
        auto_now=True,
    )

    def generate_code(self):
        code = "".join(choices("123456789", k=4))
        self.code = code
        return code

    def __str__(self) -> str:
        return f"{self.phone} - {self.code}"
