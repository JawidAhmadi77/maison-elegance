from rest_framework import serializers

from .models import OpeningHours, Restaurant


class OpeningHoursSerializer(serializers.ModelSerializer):
    weekday_label = serializers.CharField(source="get_weekday_display", read_only=True)

    class Meta:
        model = OpeningHours
        fields = ["weekday", "weekday_label", "open_time", "close_time", "is_closed"]


class RestaurantSerializer(serializers.ModelSerializer):
    opening_hours = OpeningHoursSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = [
            "id", "name", "slug", "tagline", "description", "logo_text",
            "cover_image", "address", "phone", "email", "social_links",
            "opening_hours",
        ]
