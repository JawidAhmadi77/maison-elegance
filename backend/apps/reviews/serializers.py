from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "customer_name", "rating", "text", "is_approved", "created_at"]
        read_only_fields = ["id", "created_at"]
