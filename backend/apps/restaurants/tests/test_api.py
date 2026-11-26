import pytest
from rest_framework.test import APIClient

from apps.restaurants.models import Restaurant


@pytest.mark.django_db
def test_restaurant_profile_includes_hours():
    Restaurant.objects.create(name="Maison Élégance", slug="maison-elegance")
    response = APIClient().get("/api/v1/restaurant/")
    assert response.status_code == 200
    assert response.data["name"] == "Maison Élégance"
    assert "opening_hours" in response.data


@pytest.mark.django_db
def test_restaurant_profile_missing_is_404():
    response = APIClient().get("/api/v1/restaurant/")
    assert response.status_code == 404
