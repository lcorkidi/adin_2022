from django.db import models

class Accountable(models.Model):

    code = models.CharField(
        primary_key=True,
        max_length=64,
        verbose_name='Código'
    )

    class Meta:
        app_label = 'accountables'
        verbose_name = 'Contabilizable'
        verbose_name_plural = 'Contabilizables'
