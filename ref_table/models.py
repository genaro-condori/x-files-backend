from django.db import models

class DocumentIssuerEnum(models.IntegerChoices):
    ORS = 0, 'Otro'
    CUO = 1, 'Administración de aduana'
    UCP = 2, 'Unidad de control'

class DocumentIssuer(models.Model) :
    code = models.CharField(max_length=8, verbose_name='Código')
    name = models.CharField(max_length=75, verbose_name='Description')
    type = models.IntegerField(choices=DocumentIssuerEnum.choices, default=0, verbose_name='Tipo')
    is_deleted = models.BooleanField(default=False)
	
    class Meta:
        verbose_name = 'Emisor de documentos'
        verbose_name_plural = 'Emisor de documentos'
        db_table_comment = "Emisor de documento"

class DocumentTypeEnum(models.IntegerChoices):
    SAD = 1, 'Declaración de Mercancías'
    ADM = 2, 'Actos Administrativos'

class DocumentType(models.Model):
    """Tipo de documentos"""
    code = models.CharField(max_length=7, verbose_name='Código')
    name = models.CharField(max_length=75, verbose_name='Description')
    type = models.IntegerField(choices=DocumentTypeEnum.choices, default=1, verbose_name='Tipo')
    has_dossier = models.BooleanField(default=False, verbose_name="Tiene expediente")
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'Tipos de documento'
        db_table_comment = "Tipo de Documento"

class IdTypeEnum(models.IntegerChoices):
    CI = 1, 'Cedula de Identidad'
    PAS = 2, 'Pasaporte'

class Oce(models.Model):
    """Operador de comercio exterior"""
    code = models.CharField(max_length=15, verbose_name='Código')
    name = models.CharField(max_length=100, verbose_name='Description')
    id_type = models.IntegerField(choices=IdTypeEnum.choices, blank=True, null=True, verbose_name="Tipo Id")
    legal_agent  = models.CharField(max_length=100, blank=True, null=True, verbose_name='Representante legal')
    legal_agent_id = models.CharField(max_length=15, blank=True, null=True, verbose_name='Número de identificación')
    legal_agent_doc = models.CharField(max_length=25, blank=True, null=True, verbose_name='Testimonio poder')
    legal_agent_doc_date = models.DateField(verbose_name="Testimonio fecha", null=True)
    is_deleted = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True, verbose_name="Actividad del sujeto pasivo")

    class Meta:
        verbose_name = 'Operador de Comercio Exterior'
        verbose_name_plural = 'Operadores de Comercio Exterior'
        db_table_comment = "Operador de Comercio Exterior"

class ControlType(models.Model):
    code = models.CharField(max_length=5, verbose_name='Código')
    name = models.CharField(max_length=75, verbose_name='Description')

    class Meta:
        verbose_name = 'Tipo de Control'
        verbose_name_plural = 'Tipos de Control'
        db_table_comment = 'Tipos de Control'

class ProcedureType(models.Model):
    code = models.SmallIntegerField(primary_key=True, verbose_name='Código')
    name = models.CharField(max_length=50, verbose_name='Description')
    is_request = models.BooleanField(default=False, verbose_name="Régimen solicitado")
    is_previous = models.BooleanField(default=False, verbose_name="Régimen previo")

    class Meta:
        verbose_name = 'Régimen Aduanero'
        verbose_name_plural = 'Regímenes Aduaneros'
        db_table_comment = 'Regímenes Aduaneros'
