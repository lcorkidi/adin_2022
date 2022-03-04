from django.db import models

class Accountable(models.Model):

    class Meta:
        app_label = 'accountables'
        verbose_name = 'Contabilizable'
        verbose_name_plural = 'Contabilizables'
