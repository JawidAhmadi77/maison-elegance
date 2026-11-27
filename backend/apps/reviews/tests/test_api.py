import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestReviewsAPI:
    def test_submitted_review_is_hidden_until_approved(self):
        client = APIClient()
        response = client.post(
            "/api/v1/reviews/",
            {"customer_name": "Guest", "rating": 5, "text": "Lovely evening."},
            format="json",
        )
        assert response.status_code == 201
        assert response.data["is_approved"] is False
        listing = client.get("/api/v1/reviews/")
        assert listing.data["count"] == 0

    def test_staff_sees_and_approves(self):
        staff = get_user_model().objects.create_user(
            username="host", password="pw-12345", is_staff=True
        )
        client = APIClient()
        created = client.post(
            "/api/v1/reviews/",
            {"customer_name": "Guest", "rating": 4, "text": "Very good."},
            format="json",
        ).data
        client.force_authenticate(staff)
        assert client.get("/api/v1/reviews/").data["count"] == 1
        updated = client.patch(
            f"/api/v1/reviews/{created['id']}/", {"is_approved": True}, format="json"
        )
        assert updated.status_code == 200
        client.force_authenticate(user=None)
        assert client.get("/api/v1/reviews/").data["count"] == 1

    def test_rating_out_of_range_rejected(self):
        response = APIClient().post(
            "/api/v1/reviews/",
            {"customer_name": "Guest", "rating": 9, "text": "Too good."},
            format="json",
        )
        assert response.status_code == 400
