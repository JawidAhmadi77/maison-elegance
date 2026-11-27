from rest_framework import serializers

from .models import GalleryImage


class GalleryImageSerializer(serializers.ModelSerializer):
    category_label = serializers.CharField(source="get_category_display", read_only=True)

    class Meta:
        model = GalleryImage
        fields = [
            "id", "image", "title", "description", "category",
            "category_label", "display_order", "is_active",
        ]
