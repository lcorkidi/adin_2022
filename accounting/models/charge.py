import pandas as pd
from django.db import models
from django.db.models import Sum

from adin.core.models import BaseModel
from accounting.utils.models_func import DueAge
from accounting.models.ledger import LEDGER_RECEIPT_PRIORITY

class ReportChargeManager(models.Manager):

    def accountable(self, accountable):
        objs_df=pd.DataFrame(self.get_queryset().filter(concept__accountable=accountable).values('ledger', 'account', 'account__name', 'concept__date', 'value'))        
        normalized_df=objs_df.assign(debit=objs_df.value.apply(lambda x: x if x > 0 else 0), credit=objs_df.value.apply(lambda x: -x if x < 0 else 0)).drop(['value'], axis=1)

        return normalized_df.to_dict('records')

    def get_queryset(self):
        return super().get_queryset()

class PendingChargeManager(models.Manager):
    def accountable_receivable_sum(self, accountable, account_priority):
        return self.accountable_receivable_df(accountable, account_priority)['due_value'].sum()

    def accountable_receivable_age_months(self, accountable, account_priority):
        return self.accountable_receivable_df(accountable, account_priority)['due_age'].iloc[0]

    def accountable_receivable_age_days(self, accountable, account_priority):
        return self.accountable_receivable_df(accountable, account_priority, split_months=False)['due_age'].iloc[0]

    def accountable_receivable_age_start_date(self, accountable, account_priority):
        return self.accountable_receivable_df(accountable, account_priority)['concept__date'].iloc[0]

    def accountable_receivable_dict(self, accountable, account_priority):
        if not self.get_queryset():
            return self.get_queryset()
        return self.accountable_receivable_df(accountable, account_priority).to_dict('records')

    def accountable_receivable_df(self, accountable, account_priority, split_months=True):
        objs_df=pd.DataFrame(self.get_queryset().filter(account__in=[account for account in account_priority.keys()], concept__accountable=accountable)\
            .values('id', 'ledger', 'concept__accountable', 'account', 'account__name', 'concept__date', 'value'))
        priority_df=objs_df.assign(priority=objs_df.apply(lambda x: account_priority[x.account] + LEDGER_RECEIPT_PRIORITY[x.ledger[:2]], axis=1))
        sorted_df=priority_df.sort_values(by=['concept__date', 'priority', 'value'])
        due_df=sorted_df.assign(
            due_value=sorted_df.id.apply(lambda x: Charge.objects.get(pk=x).DueValue()),
            due_age=sorted_df.concept__date.apply(lambda x: DueAge(x, split_months)))
        return due_df[due_df['due_value'] != 0]

    def get_queryset(self):
        return super().get_queryset()

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
        'accountables.Accountable_Concept',
        on_delete=models.PROTECT,
        related_name='charges',
        related_query_name='charge',
    )
    settled = models.BooleanField(
        verbose_name='Cruzado',
        default=False
    )

    objects = models.Manager()
    pending = PendingChargeManager()
    report = ReportChargeManager()

    class Meta:
        app_label = 'accounting'
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
        permissions = [
            ('activate_charge', 'Can activate charge.'),
        ]

    def DueValue(self):
        if self.ledger.type.abreviation == 'CA':
            if Charge.objects.filter(account=self.account, concept=self.concept, ledger__type__abreviation='FV', value=-self.value).exists():
                return 0
            else:
                return self.value
        elif self.ledger.type.abreviation == 'FV' and self.value < 0:
            if Charge.objects.filter(account=self.account, concept=self.concept, ledger__type__abreviation='CA', value=-self.value).exists():
                return 0        
        elif self.ledger.type.abreviation == 'FV' and self.value > 0:
            receipt = Charge.objects.filter(account=self.account, concept=self.concept, ledger__type__abreviation='RC', value__lt=0).aggregate(receipt=Sum('value'))['receipt']
            return self.value + receipt if receipt else self.value
        else:
            return 0

    def __repr__(self) -> str:
        return f'<Charge: {self.ledger}_{self.account}_{self.concept}>'

    def __str__(self) -> str:
        return f'{self.ledger}_{self.account}_{self.concept}'

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

    def create_charge(self, ledger, charge_concept, user):
        Charge(
            state_change_user=user,
            ledger=ledger,
            account=self.account,
            value=self.factor.factored_value(charge_concept.accountable, charge_concept.date, charge_concept.value, self.nature),
            concept=charge_concept
        ).save()
        
    def __repr__(self) -> str:
        return f'<Charge_Template: {self.ledger_template.code}_{self.account}-{self.get_nature_display()}-{self.factor}>'

    def __str__(self) -> str:
        return f'{self.ledger_template.code}_{self.account}-{self.get_nature_display()}-{self.factor}'
