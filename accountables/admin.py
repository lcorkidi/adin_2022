from django.contrib import admin
from .models import Accountable, Accountable_Transaction_Type, Transaction_Type, Accountable_Concept, Date_Value, Lease_Realty, Lease_Realty_Person, Lease_Realty_Realty

admin.site.register(Accountable)
admin.site.register(Accountable_Transaction_Type)
admin.site.register(Transaction_Type)
admin.site.register(Accountable_Concept)
admin.site.register(Date_Value)
admin.site.register(Lease_Realty)
admin.site.register(Lease_Realty_Person)
admin.site.register(Lease_Realty_Realty)
