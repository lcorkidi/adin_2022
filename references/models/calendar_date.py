from django.db import models

from adin.core.models import BaseModel

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

    def __repr__(self) -> str:
        return f'<Calendar_Date: {self.name}>'

    def __str__(self):
        return self.name
