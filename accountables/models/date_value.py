import datetime
from django.db import models

from adin.core.models import BaseModel
from adin.utils.data_check import errors_report

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

    @classmethod
    def get_errors_report(cls, all=False):
        return errors_report(cls, all)

    def get_obj_errors(self):
        errors = []
        # accountable (obligatory, active)
        if not self.accountable:
            errors.append(157)
        elif self.accountable.state == 0:
            errors.append(158)
        # date (obligatory, valid)
        if not self.date:
            errors.append(159)
        elif not isinstance(self.date, datetime.date):
            errors.append(160)
        # value (obligatory, positive integer)
        if not self.value:
            errors.append(161)
        elif not self.value > 0 and not isinstance(self.value, int):
            errors.append(162)
        return errors

    def __repr__(self) -> str:
        return f'<Date_Value: {self.date.strftime("%d-%m-%Y")} ${self.value} {self.accountable}>'

    def __str__(self):
        return f'{self.date.strftime("%d-%m-%Y")} ${self.value} {self.accountable}'
