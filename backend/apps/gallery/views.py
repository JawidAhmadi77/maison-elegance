from rest_framework import viewsets

from apps.core.permissions import ReadOnlyOrStaff

from .models import GalleryImage
from .serializers import GalleryImageSerializer


class GalleryImageViewSet(viewsets.ModelViewSet):
    serializer_class = GalleryImageSerializer
    permission_classes = [ReadOnlyOrStaff]
    filterset_fields = ["category"]

    def get_queryset(self):
        qs = GalleryImage.objects.all()
        if not (self.request.user and self.request.user.is_staff):
            qs = qs.filter(is_active=True)
        return qs
