from django.db import models
from adin.core.models import BaseModel

class Charge(BaseModel):

    ledger = models.ForeignKey(
        to='accounting.Ledger',
        on_delete=models.PROTECT,
        related_name='charges',
        related_query_name='charge',
        verbose_name='Registro'
    )
    account = models.ForeignKey(
        to='accounting.Account',
        on_delete=models.PROTECT,
        related_name='charges',
        related_query_name='charge',
        verbose_name='Cuenta'
    )
    value = models.IntegerField(
        verbose_name='Valor'
    )    
    concept = models.ForeignKey(
        'accounting.Charge_Concept',
        on_delete=models.PROTECT,
        related_name='charges',
        related_query_name='charge',
    )
    settled = models.BooleanField(
        verbose_name='Cruzado',
        default=False
    )

    class Meta:
        app_label = 'accounting'
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'

    def __repr__(self) -> str:
        return f'<Charge: {self.ledger.pk}_{self.account.pk}>'

    def __str__(self) -> str:
        return f'{self.ledger.pk}_{self.account.pk}'

class Charge_Concept(BaseModel):

    NATURE_CHOICE = [
        (-1, 'Crédito'),
        (1, 'Débito')
    ]

    code = models.CharField(
        max_length=128,
        primary_key=True,
        verbose_name='Código'
    )
    accountable = models.ForeignKey(
        'accountables.Accountable',
        on_delete=models.PROTECT,
        related_name='charges_concepts',
        related_query_name='charge_concept',
        verbose_name='Contabilizable'
    )
    transaction_type = models.ForeignKey(
        'references.Transaction_Type',
        on_delete=models.PROTECT,
        related_name='charges_concepts',
        related_query_name='charge_concept',
        verbose_name='Tipo Transacción'
    )
    date = models.DateField(
        verbose_name='Fecha'
    )

    class Meta:
        app_label = 'accounting'
        verbose_name = 'Concepto Movimiento'
        verbose_name_plural = 'Conceptos Movimientos'

    def __repr__(self) -> str:
        return f'<Charge_Concept: {self.code}>'

    def __str__(self) -> str:
        return self.code
