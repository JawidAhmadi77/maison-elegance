from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

api_v1 = [
    path("auth/", include("apps.accounts.urls")),
    path("", include("apps.restaurants.urls")),
    path("menu/", include("apps.menu.urls")),
    path("reservations/", include("apps.reservations.urls")),
    path("gallery/", include("apps.gallery.urls")),
    path("reviews/", include("apps.reviews.urls")),
    path("contact/", include("apps.contact.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_v1)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
