import pandas as pd
from django.db import models

from adin.core.models import BaseModel

class Phone(BaseModel):

    TYPE_CHOICE = [
        (0, 'Fijo'),
        (1, 'Movil')
    ]

    code = models.CharField(
        max_length=16,
        primary_key=True,
        verbose_name='Código'
    )
    type = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICE,
        verbose_name='Tipo'
    )
    country = models.PositiveSmallIntegerField(
        default=57,
        verbose_name='País'
    )
    region = models.PositiveSmallIntegerField(
        verbose_name='Región',
        blank=True,
        null=True,
        default=None
    )
    number = models.PositiveIntegerField(
        verbose_name='Número'
    )

    class Meta:
        app_label = 'references'
        verbose_name = 'Teléfono'
        verbose_name_plural = 'Teléfonos'
        ordering = ['code']
        constraints = [
            models.UniqueConstraint(fields=['country', 'region', 'number'], name='unique_country_region_number'),
        ]
        permissions = [
            ('activate_phone', 'Can activate phone.'),
        ]

    @classmethod
    def get_errors_report(cls, all=False):
        objs_df = pd.DataFrame(cls.objects.values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)
        errors_report = objs_df.assign(errors=objs_df[cls._meta.pk.name].apply(lambda x: cls.objects.get(pk=x).get_obj_errors()))
        if all:
            return errors_report
        return errors_report[errors_report['errors'].map(lambda x: len(x) > 0)]

    def get_obj_errors(self):
        errors = []
        # code (obligatory, length < 16)
        if not self.code:
            errors.append(90)
        elif len(self.code) > 16:
            errors.append(91)
        # type (obligatory, TYPE_CHOICE)
        if not self.type and self.type != 0:
            errors.append(54)
        elif self.type not in [x for x in range(0,len(self.TYPE_CHOICE))]:
            errors.append(55)
        # country (obligatory, psistive integer)
        if not self.country:
            errors.append(56)
        elif not self.country > 0 and not isinstance(self.country, int):
            errors.append(57)
        # region (obligatory, psistive integer)
        if not self.region:
            errors.append(56)
        elif not self.region > 0 and not isinstance(self.region, int):
            errors.append(57)
        # number (obligatory, psistive integer)
        if not self.number:
            errors.append(56)
        elif not self.number > 0 and not isinstance(self.number, int):
            errors.append(57)
        return errors

    def __repr__(self) -> str:
        return f'<Phone: {self.code}>'

    def __str__(self) -> str:
        return self.code
