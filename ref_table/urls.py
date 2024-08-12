from rest_framework.routers import DefaultRouter
# from django.urls import include, path

from .views import (
    ControlTypeViewSet,
    DocumentIssuerViewSet, DocumentTypeViewSet, 
    OceViewSet)

router = DefaultRouter()
router.register("control-type", ControlTypeViewSet, "control-type")
router.register("document-issuer", DocumentIssuerViewSet, "document-issuer")
router.register("document-type", DocumentTypeViewSet, "document-type")
router.register("oce", OceViewSet, "oce")
urlpatterns = router.urls
