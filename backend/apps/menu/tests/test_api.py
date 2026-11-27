import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from apps.menu.models import MenuCategory, MenuItem


@pytest.fixture
def menu_data(db):
    starters = MenuCategory.objects.create(name="Starters", slug="starters")
    mains = MenuCategory.objects.create(name="Main Courses", slug="main-courses")
    MenuItem.objects.create(
        category=starters, name="Seared Scallops", price="32.00",
        ingredients="Scallops, caviar", is_featured=True,
    )
    MenuItem.objects.create(
        category=mains, name="Wagyu Tenderloin", price="68.00", is_available=False,
    )
    return starters


@pytest.mark.django_db
class TestMenuAPI:
    def test_categories_listed(self, menu_data):
        response = APIClient().get("/api/v1/menu/categories/")
        assert response.status_code == 200
        assert response.data["count"] == 2

    def test_items_filter_by_category_slug(self, menu_data):
        response = APIClient().get("/api/v1/menu/items/", {"category": "starters"})
        names = [item["name"] for item in response.data["results"]]
        assert names == ["Seared Scallops"]

    def test_items_search(self, menu_data):
        response = APIClient().get("/api/v1/menu/items/", {"search": "wagyu"})
        assert response.data["count"] == 1

    def test_anonymous_cannot_create_item(self, menu_data):
        response = APIClient().post(
            "/api/v1/menu/items/",
            {"category": 1, "name": "Sneaky Dish", "price": "1.00"}, format="json",
        )
        assert response.status_code in (401, 403)

    def test_staff_can_create_item(self, menu_data):
        staff = get_user_model().objects.create_user(
            username="manager", password="pw-12345", is_staff=True
        )
        client = APIClient()
        client.force_authenticate(staff)
        response = client.post(
            "/api/v1/menu/items/",
            {"category": menu_data.id, "name": "New Dish", "price": "20.00"},
            format="json",
        )
        assert response.status_code == 201
