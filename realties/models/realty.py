from django.db import models

class Realty(models.Model):

    class Meta():
        app_label = 'realties'

    def __str__(self) -> str:
        return 'Realty'