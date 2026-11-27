from rest_framework import serializers

from .models import MenuCategory, MenuItem


class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ["id", "name", "slug", "description", "image", "display_order", "is_active"]


class MenuItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    category_slug = serializers.CharField(source="category.slug", read_only=True)
    allergen_list = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = [
            "id", "category", "category_name", "category_slug", "name",
            "description", "ingredients", "allergens", "allergen_list",
            "price", "image", "is_featured", "is_available", "display_order",
        ]

    def get_allergen_list(self, obj):
        return [a.strip() for a in obj.allergens.split(",") if a.strip()]
