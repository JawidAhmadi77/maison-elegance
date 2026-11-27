from django.contrib import admin

from .models import MenuCategory, MenuItem


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "display_order", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "price", "is_featured", "is_available"]
    list_filter = ["category", "is_featured", "is_available"]
    search_fields = ["name", "ingredients"]
    list_editable = ["price", "is_available"]
