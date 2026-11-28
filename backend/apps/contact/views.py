from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView

from apps.core.permissions import IsStaffUser

from .models import ContactMessage, NewsletterSubscriber
from .serializers import ContactMessageSerializer, NewsletterSubscribeSerializer


class ContactMessageViewSet(viewsets.ModelViewSet):
    """POST is public (throttled); reading and triage are staff-only."""

    serializer_class = ContactMessageSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "public_form"

    def get_queryset(self):
        if self.request.user and self.request.user.is_staff:
            return ContactMessage.objects.all()
        return ContactMessage.objects.none()

    def get_permissions(self):
        if self.action == "create":
            return []
        return [IsStaffUser()]

    def get_throttles(self):
        if self.action == "create":
            return super().get_throttles()
        return []

    filterset_fields = ["status"]
    search_fields = ["name", "email", "subject"]


@extend_schema(request=NewsletterSubscribeSerializer, responses={201: None})
class NewsletterSubscribeView(APIView):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "public_form"

    def post(self, request):
        serializer = NewsletterSubscribeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subscriber, created = NewsletterSubscriber.objects.get_or_create(
            email=serializer.validated_data["email"],
            defaults={"is_active": True},
        )
        if not subscriber.is_active:
            subscriber.is_active = True
            subscriber.save(update_fields=["is_active"])
        return Response(
            {"detail": "Thank you — you are on the list."},
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )
