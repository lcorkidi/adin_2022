from django.contrib import admin
from .models import Estate, Realty, Estate_Person, Realty_Estate, Appraisal

admin.site.register(Estate)
admin.site.register(Realty)
admin.site.register(Estate_Person)
admin.site.register(Realty_Estate)
admin.site.register(Appraisal)