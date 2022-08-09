import pandas as pd
from django.db import models

from adin.core.models import BaseModel

class E_Mail(BaseModel):

    e_mail = models.EmailField(
        primary_key=True,
        verbose_name='Correo Electrónico'
    )

    class Meta:
        app_label = 'references'
        verbose_name = 'Correo Electrónico'
        verbose_name_plural = 'Correos Electrónicos'
        ordering = ['e_mail']
        permissions = [
            ('e_mail', 'Can activate e-mail.'),
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
        # e_mail (obligatory)
        if not self.e_mail:
            errors.append(102)
        return errors

    def __repr__(self) -> str:
        return f'<Email: {self.e_mail}>'

    def __str__(self) -> str:
        return self.e_mail