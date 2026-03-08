from django.urls import path
from .views import InvoiceFormView

urlpatterns = [
    path('crear-factura/', InvoiceFormView.as_view(), name="issue_invoice"),
]
