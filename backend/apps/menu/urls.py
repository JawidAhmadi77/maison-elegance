from rest_framework.routers import DefaultRouter

from .views import MenuCategoryViewSet, MenuItemViewSet

router = DefaultRouter()
router.register("categories", MenuCategoryViewSet, basename="menu-category")
router.register("items", MenuItemViewSet, basename="menu-item")

urlpatterns = router.urls
