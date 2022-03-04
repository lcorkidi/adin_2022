from statistics import mode
from django.db import models

class Charge(models.Model):

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

    class Meta:
        app_label = 'accounting'
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'

class Charge_Concept(models.Model):

    accountable = models.ForeignKey(
        'accountables.Accountable',
        on_delete=models.PROTECT,
        related_name='charge_concept',
        related_query_name='charges_concept',
        verbose_name='Contabilizable'
    )

    class Meta:
        app_label = 'accounting'
        verbose_name = 'Concepto Movimiento'
        verbose_name_plural = 'Conceptos Movimientos'
