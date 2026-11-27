from django.db import models

from apps.core.models import TimeStampedModel


class GalleryImage(TimeStampedModel):
    class Category(models.TextChoices):
        FOOD = "food", "Food"
        INTERIOR = "interior", "Interior"
        KITCHEN = "kitchen", "Kitchen & Chef"
        ATMOSPHERE = "atmosphere", "Atmosphere"

    image = models.CharField(
        max_length=300, help_text="Path served by the frontend, e.g. /images/kitchen-fire.jpg"
    )
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=12, choices=Category.choices, default=Category.FOOD)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.title
