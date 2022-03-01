import imp
from django.db import models

class Phone(models.Model):

    class Meta():
        app_label = 'phones'

    def __str__(self) -> str:
        return 'Phone'