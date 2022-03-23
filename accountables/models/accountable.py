from django.db import models
from adin.core.models import BaseModel

class Accountable(BaseModel):

    code = models.CharField(
        primary_key=True,
        max_length=64,
        verbose_name='Código'
    )

    class Meta:
        app_label = 'accountables'
        verbose_name = 'Contabilizable'
        verbose_name_plural = 'Contabilizables'

    def __str__(self) -> str:
        return self.code