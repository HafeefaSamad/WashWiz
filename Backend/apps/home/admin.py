from django.contrib import admin
from .models import  Variation, Package, VehicleType

# Register your models here.
class VariationAdmin(admin.ModelAdmin):
    list_display = ['vehicle_type', 'Package', 'price']

admin.site.register( Variation)
admin.site.register( Package)
admin.site.register( VehicleType)
