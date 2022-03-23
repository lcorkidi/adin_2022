from django.db import models

from adin.core.models import BaseModel

class Date_Value(BaseModel):

    accountable = models.ForeignKey(
        'accountables.Accountable',
        on_delete=models.PROTECT,
        related_name='date_value',
        related_query_name='dates_values',
        verbose_name='Contabilizable'
    )
    date = models.DateField(
        verbose_name='Fecha'
    )
    value = models.PositiveIntegerField(
        verbose_name='Valor'
    )
                              
    class Meta:
        app_label = 'accountables'
        verbose_name = 'Fecha Valor'
        verbose_name_plural = 'Fechas Valores'
        constraints = [
            models.UniqueConstraint(fields=['accountable', 'date'], name='unique_accountable_date')
        ]

    def __repr__(self) -> str:
        return f'<Date_Value: {self.date.strftime("%d-%m-%Y")} ${self.value} {self.accountable}>'

    def __str__(self):
        return f'{self.date.strftime("%d-%m-%Y")} ${self.value} {self.accountable}'
