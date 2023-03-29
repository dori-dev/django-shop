from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=256,
    )
    category = models.ForeignKey(
        'product.Category',
        on_delete=models.CASCADE,
        related_name='products',
    )
    slug = models.SlugField(
        max_length=8,
        unique=True,
    )
    image = models.ImageField(
        upload_to='products/%Y/%m/%d/',
    )
    description = models.TextField()
    price = models.PositiveBigIntegerField()
    available = models.BooleanField(
        default=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = (
            '-updated',
        )

    def __str__(self) -> str:
        return self.name
