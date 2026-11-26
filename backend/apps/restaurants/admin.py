from django.contrib import admin

from .models import OpeningHours, Restaurant


class OpeningHoursInline(admin.TabularInline):
    model = OpeningHours
    extra = 0


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "email"]
    search_fields = ["name", "address"]
    inlines = [OpeningHoursInline]
