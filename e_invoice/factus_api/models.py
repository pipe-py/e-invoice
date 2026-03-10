from django.db import models


class Customer(models.Model):
    identification = models.CharField(
        max_length=20, unique=True, verbose_name="Identificación"
    )
    dv = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="Dígito de verificación"
    )
    company = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Razón Social"
    )
    trade_name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Nombre Comercial"
    )
    names = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Nombre"
    )
    address = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="Dirección"
    )
    email = models.EmailField(
        max_length=100, null=True, blank=True, verbose_name="email"
    )
    phone = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Teléfono"
    )
    legal_organization_id = models.PositiveIntegerField(
        verbose_name="Tipo de Organización Legal"
    )
    tribute_id = models.PositiveIntegerField(verbose_name="Responsabilidad Tributaria")
    identification_document_id = models.PositiveIntegerField(
        verbose_name="Tipo de Documento"
    )
    municipality_id = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Municipio"
    )
