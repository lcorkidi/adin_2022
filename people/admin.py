from django.contrib import admin

from .models import Person, Person_Natural, Person_Legal, Person_Address, Person_E_Mail, Person_Phone, Person_Legal_Person_Natural

admin.site.register(Person)
admin.site.register(Person_Natural)
admin.site.register(Person_Legal)
admin.site.register(Person_Address)
admin.site.register(Person_E_Mail)
admin.site.register(Person_Phone)
admin.site.register(Person_Legal_Person_Natural)