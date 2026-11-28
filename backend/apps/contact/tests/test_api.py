import pytest
from rest_framework.test import APIClient

from apps.contact.models import ContactMessage, NewsletterSubscriber


@pytest.mark.django_db
class TestContactAPI:
    def test_guest_can_send_message_but_not_read(self):
        client = APIClient()
        response = client.post(
            "/api/v1/contact/",
            {"name": "Guest", "email": "g@example.com", "subject": "Private dining",
             "message": "We are twelve for a birthday."},
            format="json",
        )
        assert response.status_code == 201
        assert ContactMessage.objects.count() == 1
        assert client.get("/api/v1/contact/").status_code in (401, 403)

    def test_newsletter_subscribe_is_idempotent(self):
        client = APIClient()
        first = client.post("/api/v1/contact/newsletter/", {"email": "a@example.com"}, format="json")
        second = client.post("/api/v1/contact/newsletter/", {"email": "a@example.com"}, format="json")
        assert first.status_code == 201
        assert second.status_code == 200
        assert NewsletterSubscriber.objects.count() == 1
