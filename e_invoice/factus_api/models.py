from django.db import models


class Customer(models.Model):
    identification = models.CharField(
        max_length=20, unique=True, verbose_name="Identificación * "
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
        verbose_name="Tipo de Organización Legal * "
    )
    tribute_id = models.PositiveIntegerField(
        verbose_name="Responsabilidad Tributaria * "
    )
    identification_document_id = models.PositiveIntegerField(
        verbose_name="Tipo de Documento *"
    )
    municipality_id = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Municipio"
    )

    def __str__(self):
        if self.company:
            if self.trade_name:
                return f"{self.company} ({self.trade_name}) - {self.identification}"
            return f"{self.company} - {self.identification}"

        if self.names:
            return f"{self.names} - {self.identification}"

        return str(self.identification)


class Establishment(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    address = models.CharField(verbose_name="Dirección", max_length=200)
    phone_number = models.CharField(verbose_name="Teléfono", max_length=20)
    email = models.EmailField(verbose_name="Email", max_length=200)
    municipality_id = models.PositiveIntegerField(verbose_name="Municipio")

    def __str__(self):
        return self.name


class Items(models.Model):
    code_reference = models.CharField(
        max_length=200, unique=True, verbose_name="Código de Referencia"
    )
    name = models.CharField(max_length=200, verbose_name="Nombre")
    quantity = models.PositiveIntegerField(verbose_name="Cantidad")
    discount_rate = models.FloatField(verbose_name="Tasa de descuento", default=0.0)
    price = models.FloatField(verbose_name="Precio")
    tax_rate = models.CharField(max_length=50, verbose_name="Tasa de Impuesto")
    unit_measure_id = models.PositiveBigIntegerField(verbose_name="Unidad de Medida")
    standard_code_id = models.PositiveIntegerField(verbose_name="Código Estándar")
    is_excluded = models.PositiveIntegerField(verbose_name="Excluido")
    tribute_id = models.PositiveIntegerField(verbose_name="Tributo")
    code = models.CharField(max_length=200, verbose_name="Código")
    withholding_tax_rate = models.FloatField(verbose_name="Porcentaje de retención")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"