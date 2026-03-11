from django.contrib import admin
from .models import (
    Customer,
    Establishment,
    Items,
)


class CustomerAdmin(admin.ModelAdmin):
    model = Customer

class EstablishmentAdmin(admin.ModelAdmin):
    model = Establishment


class ItemsAdmin(admin.ModelAdmin):
    model = Items


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Establishment, EstablishmentAdmin)
admin.site.register(Items, ItemsAdmin)