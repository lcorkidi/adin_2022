from django.contrib import admin
from .models import Account, Charge, Charge_Concept, Ledger, Ledger_Type

admin.site.register(Account)
admin.site.register(Charge)
admin.site.register(Charge_Concept)
admin.site.register(Ledger)
admin.site.register(Ledger_Type)
