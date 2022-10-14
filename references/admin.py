from django.contrib import admin
from .models import Address, E_Mail, Phone, PUC, Charge_Factor, Factor_Data, Calendar_Date

admin.site.register(Address)
admin.site.register(E_Mail)
admin.site.register(Phone)
admin.site.register(PUC)
admin.site.register(Charge_Factor)
admin.site.register(Factor_Data)
admin.site.register(Calendar_Date)
