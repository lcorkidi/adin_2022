from django.contrib import admin
from .models import Accountable, Date_Value, Lease_Realty, Lease_Realty_Person, Lease_Realty_Realty

admin.site.register(Accountable)
admin.site.register(Date_Value)
admin.site.register(Lease_Realty)
admin.site.register(Lease_Realty_Person)
admin.site.register(Lease_Realty_Realty)
