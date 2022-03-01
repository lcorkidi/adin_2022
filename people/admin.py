from django.contrib import admin

from .models import Person, Person_Natural, Person_Legal

admin.site.register(Person)
admin.site.register(Person_Natural)
admin.site.register(Person_Legal)
