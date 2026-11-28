from django.db import models

from apps.core.models import TimeStampedModel


class DiningTable(models.Model):
    name = models.CharField(max_length=60)
    capacity = models.PositiveSmallIntegerField()
    zone = models.CharField(max_length=60, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["capacity", "name"]

    def __str__(self):
        return f"{self.name} (seats {self.capacity})"


class Reservation(TimeStampedModel):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMED = "confirmed", "Confirmed"
        CANCELLED = "cancelled", "Cancelled"
        COMPLETED = "completed", "Completed"
        NO_SHOW = "no_show", "No show"

    # Only these statuses hold a table against new bookings.
    BLOCKING_STATUSES = (Status.PENDING, Status.CONFIRMED)

    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40)
    date = models.DateField(db_index=True)
    time = models.TimeField()
    guests = models.PositiveSmallIntegerField()
    table = models.ForeignKey(
        DiningTable, on_delete=models.PROTECT, related_name="reservations",
        null=True, blank=True,
    )
    special_requests = models.TextField(blank=True)
    status = models.CharField(
        max_length=12, choices=Status.choices, default=Status.PENDING, db_index=True
    )
    confirmation_code = models.CharField(max_length=12, unique=True, db_index=True)

    class Meta:
        ordering = ["date", "time"]
        indexes = [models.Index(fields=["date", "status"])]

    def __str__(self):
        return f"{self.confirmation_code} — {self.customer_name} on {self.date} {self.time}"
