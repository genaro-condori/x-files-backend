from rest_framework.routers import SimpleRouter

from .views import (
    DefControlViewSet, DefControlAttachedViewSet,
    SadViewSet, SadAttachedViewSet)

router = SimpleRouter()
router.register("def-control", DefControlViewSet, "def-control")
router.register("def-control-attach", DefControlAttachedViewSet, "def-control-attach")
router.register("sad", SadViewSet, "sad")
router.register("sad-attached", SadAttachedViewSet, "sad-attached")

urlpatterns = router.urls
