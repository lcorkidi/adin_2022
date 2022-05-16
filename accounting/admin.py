from django.contrib import admin
from .models import Account, Charge, Charge_Template, Ledger, Ledger_Type, Ledger_Template

admin.site.register(Account)
admin.site.register(Charge)
admin.site.register(Charge_Template)
admin.site.register(Ledger)
admin.site.register(Ledger_Type)
admin.site.register(Ledger_Template)
