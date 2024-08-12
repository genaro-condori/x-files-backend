from django.db import models
from ref_table.models import ControlType, DocumentIssuer, DocumentType, Oce
import uuid

# def file_location(instance, filename, **kwargs):
#     file_path = f"article/{instance.title}-{filename}"
#     return file_path    


class DefControl(models.Model):
    """
    Control Posterior
    """
    control_type =  models.ForeignKey(ControlType, on_delete=models.PROTECT, related_name='control_type' )
    ucp = models.ForeignKey(DocumentIssuer, on_delete=models.PROTECT, related_name='control_ucp' )
    oce = models.ForeignKey(Oce, on_delete=models.PROTECT, related_name='control_oce')
    reference_number = models.CharField(max_length=30)
    reference_date = models.DateField()

    
class DefControlAttached(models.Model):
    """
    Control Posterior
    Documentos adjuntos
    """
    def generate_filename(instance, filename):
        ext = filename.split('.')[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        return f"uploads/{filename}"

    ocp = models.ForeignKey(DefControl, on_delete=models.CASCADE, related_name='attached_def_control')
    documentType = models.ForeignKey(DocumentType, 
                                     on_delete=models.PROTECT, 
                                     related_name='def_control_document_type',
                                     null=True, blank=True)
    att_sender = models.ForeignKey(DocumentIssuer, on_delete=models.CASCADE, related_name='def_control_sender')
    att_ref_number = models.CharField(max_length=50, null=True, blank=True)
    att_date_issued = models.DateField(null=True, blank=True)
    att_date_notice = models.DateField(null=True, blank=True)
    att_date_submit = models.DateField(null=True, blank=True)
    att_comment = models.TextField(max_length=300, blank=True, null=True) 
    dossier_number = models.CharField(max_length=50, null=True, blank=True)

    file = models.FileField(upload_to=generate_filename, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

class Sad(models.Model):
    """
    Declaración de aduanas
    """
    def generate_filename(instance, filename):
        ext = filename.split('.')[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        return f"uploads/{filename}"

    ocp = models.ForeignKey(DefControl, on_delete=models.PROTECT, related_name='sad_def_control')
    mode = models.CharField(max_length=1, null=True, blank=True)
    customs = models.ForeignKey(DocumentIssuer, on_delete=models.PROTECT, related_name='sad_customs')
    type_proc = models.CharField(max_length=1, null=True, blank=True)
    prev_proc = models.CharField(max_length=1, null=True, blank=True)
    reference_number = models.CharField(max_length=25)
    reference_date = models.DateField()
    cif_value = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    tax_value = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    file = models.FileField(upload_to=generate_filename, null=True, blank=True)


class SadAttached(models.Model):
    """
    Declaración de aduanas
    Documentos adjuntos
    """
    def generate_filename(instance, filename):
        ext = filename.split('.')[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        return f"uploads/{filename}"
    
    sad = models.ForeignKey(Sad, on_delete=models.CASCADE, related_name='attached_sad')
    documentType = models.ForeignKey(DocumentType, 
                                     on_delete=models.PROTECT, 
                                     related_name='sad_document_type',
                                     null=True, blank=True)
    reference_number = models.CharField(max_length=50, null=True, blank=True)
    reference_date = models.DateField(null=True, blank=True)
    file = models.FileField(upload_to=generate_filename, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
