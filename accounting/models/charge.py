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
        permissions = [
            ('activate_charge', 'Can activate charge.'),
        ]

    def __repr__(self) -> str:
        return f'<Charge: {self.ledger}_{self.account}_{self.concept}>'

    def __str__(self) -> str:
        return f'{self.ledger}_{self.account}_{self.concept}'

class Charge_Concept(BaseModel):

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

class Charge_Template(BaseModel):

    NATURE_CHOICE = [
        (-1, 'Crédito'),
        (1, 'Débito')
    ]

    ledger_template = models.ForeignKey(
        'accounting.Ledger_Template',
        on_delete=models.PROTECT,
        related_name='charges_templates',
        related_query_name='charge_template',
        verbose_name='Formato Registro'
    )
    account = models.ForeignKey(
        'accounting.Account',
        on_delete=models.PROTECT,
        related_name='charges_templates',
        related_query_name='charge_template',
        verbose_name='Cuenta'
    )
    nature = models.IntegerField(
        choices=NATURE_CHOICE,
        verbose_name='Naturaleza'
    )
    factor = models.ForeignKey(
        'references.Charge_Factor',
        on_delete=models.PROTECT,
        related_name='charges_templates',
        related_query_name='charge_template',
        verbose_name='Tasa'
    )

    class Meta:
        app_label = 'accounting'
        verbose_name = 'Formato Movimiento'
        verbose_name_plural = 'Formatos Movimientos'

    def charge_from__template(self, ledger, charge_concept, user):
        Charge(
            state_change_user=user,
            ledger=ledger,
            account=self.account,
            value=self.factor.factored_value(charge_concept.accountable, charge_concept.date, charge_concept.accountable.subclass_obj().date_value_dict()[charge_concept.date], self.nature),
            concept=charge_concept
        ).save()
        
    def __repr__(self) -> str:
        return f'<Charge_Template: {self.ledger_template.code}_{self.account}-{self.get_nature_display()}-{self.factor}>'

    def __str__(self) -> str:
        return f'{self.ledger_template.code}_{self.account}-{self.get_nature_display()}-{self.factor}'
