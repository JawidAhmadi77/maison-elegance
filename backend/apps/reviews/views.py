from rest_framework import viewsets
from rest_framework.throttling import ScopedRateThrottle

from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """Guests read approved reviews and submit new ones (unapproved
    until a staff member moderates them). Staff see everything."""

    serializer_class = ReviewSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "public_form"

    def get_queryset(self):
        if self.request.user and self.request.user.is_staff:
            return Review.objects.all()
        return Review.objects.filter(is_approved=True)

    def perform_create(self, serializer):
        # Whatever the payload claims, a guest submission starts unapproved.
        serializer.save(is_approved=False)

    def get_permissions(self):
        from rest_framework.permissions import IsAdminUser

        if self.action in ("update", "partial_update", "destroy"):
            return [IsAdminUser()]
        return super().get_permissions()

    def get_throttles(self):
        if self.action == "create":
            return super().get_throttles()
        return []
