from django.contrib import admin

from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "display_order", "is_active"]
    list_filter = ["category", "is_active"]
    search_fields = ["title"]
