from django.db import models

class Appraisal(models.Model):

    TYPE_CHOICE = [
        (0, 'Catastral'),
        (1, 'Comercial')
    ]

    estate = models.ForeignKey(
        'properties.Estate',
        on_delete=models.CASCADE,
        verbose_name='Predio'
    )
    type = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICE,
        verbose_name='Tipo'
    )
    date = models.DateField(
        verbose_name='Fecha'
    )
    value = models.PositiveBigIntegerField(
        verbose_name='Valor'
    )

    class Meta:
        app_label = 'properties'
        verbose_name = 'Avaluo'
        verbose_name_plural = 'Avaluos'

    def __repr__(self) -> str:
        return f'<Appraisal: {self.get_type_display()}_{self.date}_{self.value}>'

    def __str__(self) -> str:
        return f'{self.get_type_display()}_{self.date}_{self.value}'