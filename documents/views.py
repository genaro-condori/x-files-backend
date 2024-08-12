from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    DefControl, DefControlAttached, 
    Sad, SadAttached)
from .serializers import (
    DefControlSerializer, DefControlAttachedSerializer, 
    SadSerializer, SadAttachedSerializer)

# class ConfigDepthViewSet(viewsets.ModelViewSet):

#     def get_serializer_context(self):
#         context = super().get_serializer_context()
        
#         # if self.action in ["create", "update", "partial_update", "destroy"]:        
#         if self.action in ['list', 'retrieve']:
#             context['depth'] = 1

#         return context
    

class DefControlViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = DefControl.objects.all()
    serializer_class = DefControlSerializer

class DefControlAttachedViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = DefControlAttached.objects.order_by('-att_date_issued').all()
    serializer_class = DefControlAttachedSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields  = ['ocp', 'is_deleted']

class SadViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Sad.objects.all()
    serializer_class = SadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields  = ['ocp', 'is_deleted']

class SadAttachedViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = SadAttached.objects.order_by('reference_date').all()
    serializer_class = SadAttachedSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields  = ['sad', 'is_deleted']
