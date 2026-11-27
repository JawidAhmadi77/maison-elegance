from django.db import models

from apps.core.models import TimeStampedModel


class MenuCategory(TimeStampedModel):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=300, blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name_plural = "Menu categories"

    def __str__(self):
        return self.name


class MenuItem(TimeStampedModel):
    category = models.ForeignKey(
        MenuCategory, on_delete=models.CASCADE, related_name="items"
    )
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    ingredients = models.CharField(max_length=300, blank=True)
    allergens = models.CharField(
        max_length=200, blank=True, help_text="Comma-separated, e.g. gluten, shellfish"
    )
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.CharField(max_length=300, blank=True)
    is_featured = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["category__display_order", "display_order", "name"]
        indexes = [
            models.Index(fields=["is_featured", "is_available"]),
            models.Index(fields=["category", "is_available"]),
        ]

    def __str__(self):
        return self.name
