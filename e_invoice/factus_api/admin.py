from django.contrib import admin
from .models import Customer, Establishment


class CustomerAdmin(admin.ModelAdmin):
    model = Customer

class EstablishmentAdmin(admin.ModelAdmin):
    model = Establishment
    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Establishment, EstablishmentAdmin)