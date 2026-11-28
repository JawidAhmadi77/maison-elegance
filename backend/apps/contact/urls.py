from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ContactMessageViewSet, NewsletterSubscribeView

router = DefaultRouter()
router.register("", ContactMessageViewSet, basename="contact")

urlpatterns = [
    path("newsletter/", NewsletterSubscribeView.as_view(), name="newsletter-subscribe"),
] + router.urls
