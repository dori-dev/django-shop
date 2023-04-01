from django.db import models


class Category(models.Model):
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,
    )
    is_child = models.BooleanField(
        default=False,
    )
    name = models.CharField(
        max_length=256,
    )
    slug = models.SlugField(
        max_length=256,
        unique=True,
    )

    class Meta:
        ordering = [
            'name',
        ]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name
