from django.contrib import admin
from .models import  Variation, Package, VehicleType, Category,Slot

# Register your models here.
class VariationAdmin(admin.ModelAdmin):
    list_display = ['id', 'package', 'price']

admin.site.register( Variation,VariationAdmin)
admin.site.register( Package)
admin.site.register( VehicleType)
admin.site.register( Category)
admin.site.register( Slot)


