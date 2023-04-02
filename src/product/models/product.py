from random import choices
from string import ascii_letters

from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(
        max_length=256,
    )
    category = models.ManyToManyField(
        'product.Category',
        related_name='products',
    )
    slug = models.SlugField(
        max_length=8,
        blank=True,
        null=True,
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

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = self._generate_slug()
            while Product.objects.filter(slug=slug).exists():
                slug = self._generate_slug()
            self.slug = slug
        return super().save(*args, **kwargs)

    @staticmethod
    def _generate_slug(length=8):
        return "".join(
            choices(ascii_letters, k=length)
        )

    def get_absolute_url(self):
        return reverse('product:detail', args=(self.slug,))

    def __str__(self) -> str:
        return self.name
