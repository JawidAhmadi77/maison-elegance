from django.contrib import admin

from .models import DiningTable, Reservation


@admin.register(DiningTable)
class DiningTableAdmin(admin.ModelAdmin):
    list_display = ["name", "capacity", "zone", "is_active"]
    list_filter = ["is_active", "zone"]
    search_fields = ["name"]


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        "confirmation_code", "customer_name", "date", "time", "guests",
        "table", "status",
    ]
    list_filter = ["status", "date"]
    search_fields = ["customer_name", "email", "confirmation_code", "phone"]
    date_hierarchy = "date"
