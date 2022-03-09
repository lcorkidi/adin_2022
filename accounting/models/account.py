from django.db import models
from accounting.core import Account_Structure
from adin.core.models import BaseModel

class Account(BaseModel):
    
    code = models.PositiveBigIntegerField(
        primary_key=True,
        verbose_name='Código'
    )
    name = models.CharField(
        max_length=128,
        blank=True,
        verbose_name='Nombre'
    )

    class Meta:
        app_label = 'accounting'
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'

    @property
    def levels(self):
        return Account_Structure.levels(self.code)

    @property
    def nature(self):
        return Account_Structure.nature(self.code)

    def __repr__(self) -> str:
        return f'<Acc: {self.code}>'
    
    def __str__(self) -> str:
        return self.code