from django.db import models
from adin.core.models import BaseModel

class Ledger(BaseModel):

    code = models.CharField(
        primary_key=True,
        max_length=64,
        verbose_name='Código'
    )
    type = models.ForeignKey(
        'accounting.Ledger_Type',
        on_delete=models.PROTECT,
        related_name='ledgers',
        related_query_name='ledger',
        verbose_name='Tipo'
    )
    consecutive = models.PositiveIntegerField(
        verbose_name='Consecutivo'
    )
    description = models.TextField(
        max_length=255,
        verbose_name='Descripción',
        blank=True,
        null=True,
        default=None
    )
    holder = models.ForeignKey(
        'people.Person',
        on_delete=models.PROTECT,
        related_name='ledgers_holders',
        related_query_name='ledger_holder',
        verbose_name='Titular'
    )    
    third_party = models.ForeignKey(
        'people.Person',
        on_delete=models.PROTECT,
        related_name='ledgers_third_parties',
        related_query_name='ledger_third_party',
        verbose_name='Tercero'
    )
    date = models.DateField(
        verbose_name='Fecha'
    )

    class Meta:
        app_label = 'accounting'
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
        constraints = [
            models.UniqueConstraint(fields=['type', 'consecutive'], name='unique_type_consecutive'),
        ]
        permissions = [
            ('activate_ledger', 'Can activate ledger.'),
        ]

    def __repr__(self) -> str:
        return f'<Ledger: {self.code}^{self.date.strftime("%Y-%m-%d")}_{self.third_party}>'

    def __str__(self) -> str:
        return f'{self.code}^{self.date.strftime("%Y-%m-%d")}_{self.third_party}'

class Ledger_Type(BaseModel):
    
    name =  models.CharField(
        max_length=64,
        primary_key=True,
        verbose_name='Nombre'
    )
    abreviation =  models.CharField(
        max_length=4,
        verbose_name='Abreviación'
    )
    

    class Meta:
        app_label = 'accounting'
        verbose_name = 'Registro Tipo'
        verbose_name_plural = 'Registros Tipos'

    def __repr__(self) -> str:
        return f'<Ledger_Type: {self.name}>'
    
    def __str__(self) -> str:
        return self.name