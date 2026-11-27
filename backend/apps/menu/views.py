import django_filters
from rest_framework import viewsets

from apps.core.permissions import ReadOnlyOrStaff

from .models import MenuCategory, MenuItem
from .serializers import MenuCategorySerializer, MenuItemSerializer


class MenuItemFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name="category__slug")
    featured = django_filters.BooleanFilter(field_name="is_featured")

    class Meta:
        model = MenuItem
        fields = ["category", "featured", "is_available"]


class MenuCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = MenuCategorySerializer
    permission_classes = [ReadOnlyOrStaff]
    lookup_field = "slug"

    def get_queryset(self):
        qs = MenuCategory.objects.all()
        if not (self.request.user and self.request.user.is_staff):
            qs = qs.filter(is_active=True)
        return qs


class MenuItemViewSet(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    permission_classes = [ReadOnlyOrStaff]
    filterset_class = MenuItemFilter
    search_fields = ["name", "description", "ingredients"]
    ordering_fields = ["price", "display_order", "name"]

    def get_queryset(self):
        qs = MenuItem.objects.select_related("category")
        if not (self.request.user and self.request.user.is_staff):
            qs = qs.filter(category__is_active=True)
        return qs
