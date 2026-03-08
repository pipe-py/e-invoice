from django.shortcuts import render
from django.views import generic
from .form import InvoiceForm


class InvoiceFormView(generic.FormView):
    template_name = "invoice/issue_invoice.html"
    form_class = InvoiceForm