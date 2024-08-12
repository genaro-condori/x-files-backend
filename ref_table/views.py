from rest_framework import filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend


from .models import (
    ControlType, DocumentIssuer, DocumentType, Oce)

from .serializers import (
    ControlTypeSerializer, DocumentIssuerSerializer, DocumentTypeSerializer, 
    OceSerializer)

class ControlTypeViewSet(viewsets.ModelViewSet):
    """
    Tipos de control
    """
    queryset = ControlType.objects.order_by('name').all()
    serializer_class = ControlTypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    ordering_fields  = ['name']

class DocumentIssuerViewSet(viewsets.ModelViewSet):
    """
    Administraciones de aduana
    """
    queryset = DocumentIssuer.objects.order_by('name').all()
    serializer_class = DocumentIssuerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','type']
    ordering_fields  = ['name']

class DocumentTypeViewSet(viewsets.ModelViewSet):
    """
    Tipo de documento.
    """
    queryset = DocumentType.objects.order_by('name').all()
    serializer_class = DocumentTypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields  = ['name', "type", "is_deleted"]
    ordering_fields  = ['name']

class OceViewSet(viewsets.ModelViewSet):
    """
    Operador de comercio exterior.
    """
    queryset = Oce.objects.order_by('name').all()
    serializer_class = OceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    ordering_fields  = ['name']
