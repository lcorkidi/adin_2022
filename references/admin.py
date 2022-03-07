from django.contrib import admin
from .models import Address, Email, Phone, PUC, Transaction_Type

admin.site.register(Address)
admin.site.register(Email)
admin.site.register(Phone)
admin.site.register(PUC)
admin.site.register(Transaction_Type)
