import pandas as pd
from django.db import models

from adin.core.models import BaseModel

class PUC(BaseModel):

    code = models.PositiveBigIntegerField( 
        primary_key=True,
        verbose_name='Cuenta'
        )
    name = models.CharField(
        max_length=100,
        verbose_name='Nombre'
        )

    class Meta:
        app_label = 'references'
        verbose_name = 'Cuenta PUC'
        verbose_name_plural = 'Cuentas PUC'

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
            errors.append(103)
        elif not self.code > 0 and not isinstance(self.country, int):
            errors.append(104)
        # name (obligatory, length < 101)
        if not self.name:
            errors.append(105)
        elif len(self.name) > 100:
            errors.append(106)
        return errors

    def __repr__(self) -> str:
        return f'<Puc: {self.code}>'

    def __str__(self):
        return self.code
