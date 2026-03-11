from django import forms
from core.utils.constants import CODE_TABLES
from factus_api.models import Customer, Items


class InvoiceForm(forms.Form):
    # Customer
    numbering_range_id = forms.ChoiceField(label="Rango de numeración", choices=())
    reference_code = forms.CharField(label="Código de referencia")
    client = forms.ModelChoiceField(
        label="Cliente",
        queryset=Customer.objects.all(),
        empty_label="Seleccione un Cliente",
    )
    product = forms.ModelChoiceField(
        label="Producto",
        queryset=Items.objects.all(),
        empty_label="Seleccione un Producto",
    )
    payment_method = forms.ChoiceField(label="Método de pago", choices=())
    observation = forms.CharField(label="Observaciones", widget=forms.Textarea)
