from rest_framework import serializers

from .models import (
    DefControl, DefControlAttached, 
    Sad, SadAttached)

from ref_table.serializers import (
    ControlTypeSerializer,
    DocumentIssuerSerializer, DocumentTypeSerializer, 
    OceSerializer)

class DefControlSerializer(serializers.ModelSerializer):
    # Formas de recuperar datos de las tablas relacionadas
    # ucp = UcpSerializer(read_only=True)
    # oce = OceSerializer(read_only=True)
    # ucp_name = serializers.CharField(source='ucp.name')
    # oce_name = serializers.CharField(source='oce.name')
    # sad = SadSerializer(many=True, source="sad_deffered_control")

    class Meta:
        model = DefControl
        fields = [
            "id",
            "control_type",
            "ucp",
            "oce", 
            "reference_number",
            "reference_date"
        ]


    def __init__(self, *args, **kwargs):

        is_list = False

        if 'context' in kwargs:
            action = kwargs['context']['view'].action
            is_list = action == 'list'
        else:
            is_list = True

        if is_list:
            self.fields['control_type'] = ControlTypeSerializer(fields=('code', 'name'))
            self.fields['ucp'] = DocumentIssuerSerializer(fields=('code', 'name'))
            self.fields['oce'] = OceSerializer(fields=('code', 'name'))

        super().__init__(*args, **kwargs)


class DefControlAttachedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DefControlAttached
        fields = (
            "id",
            "ocp",
            "documentType",
            "att_sender",
            "att_ref_number",
            "att_date_issued",
            "att_date_notice",
            "att_date_submit",
            "att_comment",
            "dossier_number",
            "file"
        )

    def __init__(self, *args, **kwargs):

        is_list = False

        if 'context' in kwargs:
            action = kwargs['context']['view'].action
            is_list = action == 'list'
        else:
            is_list = True

        if is_list:
            self.fields['documentType'] = DocumentTypeSerializer()
        
        super().__init__(*args, **kwargs)


class SadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sad
        fields = [
            "id",
            "ocp",
            "mode",
            "customs",
            "type_proc",
            "prev_proc",
            "reference_number",
            "reference_date",
            "cif_value",
            "tax_value",
            "file"
        ]

    def __init__(self, *args, **kwargs):

        is_list = False

        if 'context' in kwargs:
            action = kwargs['context']['view'].action
            is_list = action == 'list'
        else:
            is_list = True

        fields = None
        if is_list:
            fields = ["id", "customs", "reference_number",  "reference_date", "file"]
        
        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)
        
        if fields is not None:
            # Drop any fields that are not specified in the `fields`
            # argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


        if is_list:
            self.fields['customs'] = DocumentIssuerSerializer(fields=('code', 'name'))

        super().__init__(*args, **kwargs)
class SadAttachedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SadAttached
        fields = (
            "id",
            "sad",
            "documentType",
            "reference_number",
            "reference_date",
            "file"
        )

    def __init__(self, *args, **kwargs):

        is_list = False

        if 'context' in kwargs:
            action = kwargs['context']['view'].action
            is_list = action == 'list'
        else:
            is_list = True

        if is_list:
            self.fields['documentType'] = DocumentTypeSerializer()
        
        super().__init__(*args, **kwargs)
