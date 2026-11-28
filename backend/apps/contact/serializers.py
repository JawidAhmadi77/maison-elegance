from rest_framework import serializers

from .models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ["id", "name", "email", "subject", "message", "status", "created_at"]
        read_only_fields = ["id", "status", "created_at"]


class NewsletterSubscribeSerializer(serializers.Serializer):
    # Plain serializer on purpose: the model field is unique, and a
    # ModelSerializer would reject a returning subscriber with a 400
    # before the view can answer "already on the list".
    email = serializers.EmailField()
