from django.db import models

class Appraisal(models.Model):

    TYPE_CHOICE = [
        (0, 'Catastral'),
        (1, 'Comercial')
    ]

    type = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICE,
        verbose_name='Tipo'
    )
    date = models.DateField(
        verbose_name='Fecha'
    )
    value = models.FloatField(
        verbose_name='Valor'
    )

    class Meta:
        app_label = 'references'
        verbose_name = 'Avaluo'
        verbose_name_plural = 'Avaluos'

    def __str__(self) -> str:
        return f'<Appraisal: {self.type}-{self.date}-{self.value}>'