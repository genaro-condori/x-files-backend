from rest_framework import serializers
from .models import (ControlType, DocumentIssuer, DocumentType, Oce)

class DynamicSerializer (serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if exclude is not None:
            not_allowed = set(exclude)
            for field_name in not_allowed:
                self.fields.pop(field_name)

class ControlTypeSerializer(DynamicSerializer):
    class Meta:
        model = ControlType
        fields = [
            "id",
            "code",
            "name",
        ]


class DocumentIssuerSerializer(DynamicSerializer):
    class Meta:
        model = DocumentIssuer
        fields = [
            "id",
            "code",
            "name",
            "type"
        ]

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = [
            "id",
            "code",
            "name",
            "type",
            "has_dossier"
        ]

class OceSerializer(DynamicSerializer):
    class Meta:
        model = Oce
        fields = [
            "id",
            "code",
            "name",
            "legal_agent",
            "legal_agent_id",
            "legal_agent_doc",
            "legal_agent_doc_date",
            "note"
        ]
