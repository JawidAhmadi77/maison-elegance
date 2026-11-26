from django.db import models

from apps.core.models import TimeStampedModel


class Restaurant(TimeStampedModel):
    """The restaurant itself. Kept to a single row in practice;
    the API always serves the first record."""

    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    tagline = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    logo_text = models.CharField(
        max_length=120, blank=True, help_text="Wordmark text, e.g. Maison Élégance"
    )
    cover_image = models.CharField(
        max_length=300, blank=True, help_text="Path served by the frontend, e.g. /images/hero-interior.jpg"
    )
    address = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    social_links = models.JSONField(
        default=dict, blank=True, help_text='{"instagram": "https://...", "facebook": "..."}'
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class OpeningHours(models.Model):
    """One row per weekday. A closed day has is_closed=True and no times."""

    WEEKDAYS = [
        (0, "Monday"), (1, "Tuesday"), (2, "Wednesday"), (3, "Thursday"),
        (4, "Friday"), (5, "Saturday"), (6, "Sunday"),
    ]

    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="opening_hours"
    )
    weekday = models.PositiveSmallIntegerField(choices=WEEKDAYS)
    open_time = models.TimeField(null=True, blank=True)
    close_time = models.TimeField(null=True, blank=True)
    is_closed = models.BooleanField(default=False)

    class Meta:
        ordering = ["weekday"]
        unique_together = ("restaurant", "weekday")
        verbose_name_plural = "Opening hours"

    def __str__(self):
        if self.is_closed:
            return f"{self.get_weekday_display()}: closed"
        return f"{self.get_weekday_display()}: {self.open_time} – {self.close_time}"
