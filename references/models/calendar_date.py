from datetime import datetime
from django.db import models

from adin.core.models import BaseModel
from adin.utils.data_check import errors_report

class Calendar_Date(BaseModel):

    name = models.CharField(
        max_length=63,
        primary_key=True,
        verbose_name='Descripción'
    )
    date = models.DateField(
        verbose_name='Fecha'
    )

    class Meta:
        app_label = 'references'
        verbose_name = 'Fecha Calendario'
        verbose_name_plural = 'Fechas Calendario'
        ordering = ['name']
        permissions = [
            ('calendar_date', 'Can activate calendar_date.'),
        ]

    @classmethod
    def get_errors_report(cls, all=False):
        return errors_report(cls, all)

    def get_obj_errors(self):
        errors = []
        # name (obligatory, length < 64)
        if not self.name:
            errors.append
        elif len(self.name) > 63:
            errors.append(87)
        # date (obligatory, date)
        if not self.date:
            errors.append(88)
        if isinstance(self.date, datetime):
            errors.append(89)
        return errors

    def __repr__(self) -> str:
        return f'<Calendar_Date: {self.name}>'

    def __str__(self):
        return self.name
