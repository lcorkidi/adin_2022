from django.contrib import admin
from .models import Address, E_Mail, Phone, PUC, Transaction_Type, Charge_Factor

admin.site.register(Address)
admin.site.register(E_Mail)
admin.site.register(Phone)
admin.site.register(PUC)
admin.site.register(Transaction_Type)
admin.site.register(Charge_Factor)
