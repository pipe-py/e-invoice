from django import forms
from core.utils.constants import CODE_TABLES


class InvoiceForm(forms.Form):
    # Customer
    numbering_range_id = forms.ChoiceField(label="Rango de numeración", choices=())
    reference_code = forms.CharField(label="Código de referencia")
    client = forms.ChoiceField(label="Cliente", choices=())
    product = forms.ChoiceField(label="Producto", choices=())
    payment_method = forms.ChoiceField(label="Método de pago", choices=())
    observation = forms.CharField(label="Observaciones", widget=forms.Textarea)