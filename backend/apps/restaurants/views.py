from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.permissions import ReadOnlyOrStaff

from .models import Restaurant
from .serializers import RestaurantSerializer


@extend_schema(responses={200: RestaurantSerializer})
class RestaurantView(APIView):
    """GET serves the (single) restaurant profile; staff may PATCH it."""

    permission_classes = [ReadOnlyOrStaff]

    def get(self, request):
        restaurant = Restaurant.objects.prefetch_related("opening_hours").first()
        if restaurant is None:
            return Response({"detail": "Restaurant profile is not set up yet."}, status=404)
        return Response(RestaurantSerializer(restaurant).data)

    def patch(self, request):
        restaurant = Restaurant.objects.first()
        if restaurant is None:
            return Response({"detail": "Restaurant profile is not set up yet."}, status=404)
        serializer = RestaurantSerializer(restaurant, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class RestaurantAdminViewSet(viewsets.ModelViewSet):
    """Full CRUD for staff tooling; the public surface stays RestaurantView."""

    queryset = Restaurant.objects.prefetch_related("opening_hours")
    serializer_class = RestaurantSerializer
    permission_classes = [ReadOnlyOrStaff]
