from django.db import models
from django.contrib.contenttypes.models import ContentType

from adin.core.models import BaseModel

class Accountable(BaseModel):

    code = models.CharField(
        primary_key=True,
        max_length=64,
        verbose_name='Código'
    )
    subclass = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
        verbose_name='Subclase'
    )
    transaction_types = models.ManyToManyField(
        'accountables.Accountable_Transaction_Type',
        related_name='accountables',
        related_query_name='accountable',
        verbose_name='Tipos de Cargo'
    )

    class Meta:
        app_label = 'accountables'
        verbose_name = 'Contabilizable'
        permissions = [
            ('accounting_accountable', 'Can do accountable accounting.')
        ]

    def subclass_obj(self):
        return self.subclass.model_class().active.get(code=self.code)

    def __repr__(self) -> str:
        return f'<Accountable: {self.code}>'

    def __str__(self) -> str:
        return self.code

class Accountable_Transaction_Type(BaseModel):

    name =  models.CharField(
        max_length=64,
        primary_key=True,
        verbose_name='Nombre'
    )

    class Meta:
        app_label = 'accountables'
        verbose_name = 'Transacción Tipo'
        verbose_name_plural = 'Transacciones Tipos'
        permissions = [
            ('activate_transaction_type', 'Can activate transaction type.'),
        ]

    def __repr__(self) -> str:
        return f'<Transaction: {self.name}>'
    
    def __str__(self) -> str:
        return self.name

class Accountable_Concept(BaseModel):

    code = models.CharField(
        max_length=128,
        primary_key=True,
        verbose_name='Código'
    )
    accountable = models.ForeignKey(
        Accountable,
        on_delete=models.PROTECT,
        related_name='accountable_concept',
        related_query_name='accountable_concepts',
        verbose_name='Contabilizable'
    )
    transaction_type = models.ForeignKey(
        Accountable_Transaction_Type,
        on_delete=models.PROTECT,
        related_name='accountable_concept',
        related_query_name='accountable_concepts',
        verbose_name='Tipo Transacción'
    )
    date = models.DateField(
        verbose_name='Fecha'
    )

    class Meta:
        app_label = 'accountables'
        verbose_name = 'Concepto Movimiento'
        verbose_name_plural = 'Conceptos Movimientos'

    # def check_in_ledger(self, ledger_template):
    #     charges_df = pd.DataFrame(Charge.active.filter(concept=self, ledger__type=ledger_template.ledger_type).values('ledger', 'account', 'value'))
    #     if charges_df.empty:
    #         return False
    #     else:
    #         if charges_df.ledger.nunique() != 1:
    #             return f'{self} in multiple ledgers ({charges_df.ledger.unique()[0]}).'
    #         base_value = self.accountable.date_value_dict()[self.date]
    #         account_value_dict = {}
    #         for charge_template in ledger_template.charges_templates.all():
    #             account_value_dict[charge_template.account_id] = charge_template.factor.factored_value(self.accountable, self.date, base_value, charge_template.nature)
    #         charges_df = charges_df.assign(correct=charges_df.apply(lambda x: True if account_value_dict[x.account] == x.value else False, axis=1)) 
    #         if len(charges_df) == charges_df.correct.value_counts()[True]:
    #             return True
    #         else:
    #             return charges_df

    def __repr__(self) -> str:
        return f'<Charge_Concept: {self.code}>'

    def __str__(self) -> str:
        return self.code
