from django.contrib import admin
from . models import Account

# Register your models here.


class AcoountAdmin(admin.ModelAdmin):
    list_display = ['email' , 'username', 'Phone_number','id']


admin.site.register(Account, AcoountAdmin)
