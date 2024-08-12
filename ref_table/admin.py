from django.contrib import admin
from .models import (
    ControlType,
    DocumentIssuer, DocumentType, 
    Oce, ProcedureType
)

@admin.register(ControlType)
class ControlTypeAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
    search_fields = ['name']
    ordering = ['name']

@admin.register(DocumentIssuer)
class DocumentIssuerAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'type']
    list_filter = ['type']
    search_fields = ['name']
    ordering = ['name']

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'type']
    list_filter = ['type']
    search_fields = ['name']
    ordering = ['name']

@admin.register(Oce)
class OceAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
    search_fields = ['name']
    ordering = ['name']

@admin.register(ProcedureType)
class ProcedureTypeAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'is_request', 'is_previous']
    search_fields = ['name']
    ordering = ['name']
