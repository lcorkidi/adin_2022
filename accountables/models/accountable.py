import pandas as pd
from django.db import models
from django.contrib.contenttypes.models import ContentType

from adin.core.models import BaseModel
from adin.utils.data_check import errors_report
from accountables.utils import accon_2_code

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

    @classmethod
    def get_errors_report(cls, all=False):
        return errors_report(cls, all)

    def ledger_holder(self):
        return self.subclass_obj().primary_lessor()

    def ledger_third_party(self):
        return self.subclass_obj().lessee()

    def subclass_obj(self):
        return self.subclass.model_class().active.get(code=self.code)

    def clean_value(self, value):
        return self.subclass_obj().clean_value(value)

    def get_obj_errors(self):
        return self.subclass_obj().get_obj_errors()

    def get_date_value_errors(self):
        return self.subclass_obj().get_date_value_errors()

    def pending_concept_date_values(self, transaction_type, first_date=None, extra_months=0):
        return self.subclass_obj().pending_concept_date_values(transaction_type)

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
            ('activate_accountable_transaction_type', 'Can activate transaction type.'),
            ('check_accountable_transaction_type', 'Can check transaction type.'),
        ]

    @classmethod
    def get_errors_report(cls, all=False):
        return errors_report(cls, all)

    def get_obj_errors(self):
        errors = []
        # name (obligatory, length > 64)
        if not self.name:
            errors.append(155)
        elif len(self.name) > 64:
            errors.append(156)
        return errors

    def __repr__(self) -> str:
        return f'<Transaction: {self.name}>'
    
    def __str__(self) -> str:
        return self.name

class Accountable_ConceptPendingManager(models.Manager):

    def charge(self, acc, led_tem):
        qs = self.get_queryset().filter(accountable=acc)
        objs_df = pd.DataFrame(qs.values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)
        pending_charge_df=objs_df.assign(pending_charge=objs_df.code.apply(lambda x: qs.get(pk=x).Pending_Charge(led_tem)))
        pending_charge_list=list(pending_charge_df[pending_charge_df['pending_charge']==True]['code'])
        return qs.filter(code__in=pending_charge_list)

    def get_queryset(self):
        return super().get_queryset().exclude(state=0)

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
    value = models.PositiveIntegerField(
        verbose_name='Valor'
    )
    value_relation = models.ForeignKey(
        'accountables.Date_Value',
        on_delete=models.PROTECT,
        related_name='accountable_concept',
        related_query_name='accountable_concepts',
        verbose_name='Fecha Valor',
        null=True,
        blank=True,
        default=None,
    )

    objects = models.Manager()
    pending = Accountable_ConceptPendingManager()

    class Meta:
        app_label = 'accountables'
        verbose_name = 'Concepto Contabilizable'
        verbose_name_plural = 'Conceptos Contabilizables'

    def Pending_Charge(self, led_tem):
        from accounting.models import Charge

        for cha_tem in led_tem.charges_templates.all():
            if not Charge.objects.filter(
                account=cha_tem.account,
                value=cha_tem.factor.factored_value(self.accountable, self.date, self.value, cha_tem.nature),
                concept=self
            ).exists():
                return True
        return False

    def get_obj_errors(self):
        errors = []
        # code (obligatory, function of attributes)
        if not self.code:
            errors.append(163)
        else:
            if self.code != accon_2_code(self):
                errors.append(164)
        # accountable (obligatory, active)
        if not self.accountable:
            errors.append(165)
        else:
            if self.accountable.state == 0:
                errors.append(166)
        # transaction_type (obligatory, active, related to accountable)
        if not self.transaction_type:
            errors.append(167)
        else:
            if self.transaction_type.state == 0:
                errors.append(168)
            if self.transaction_type not in self.accountable.transaction_type.exclude(state=0):
                errors.append(169) 
        # date (obligatory, proper accountable date)
        if not self.date:
            errors.append(170)
        else:
            if self.date not in self.accountable.monthly_dates():
                errors.append(171) 
        # value (obligatory, positive integer, proper accountable value)
        if not self.value:
            errors.append(172)
        else:
            if not (self.value > 0 and isinstance(self.value, int)):
                errors.append(173)
            if self.value != {dt: self.accountable.subclass_obj().get_value_4_date(dt) for dt in self.accountable.subclass_obj().monthly_dates()}[self.date]:
                errors.append(174) 
        return errors

    def __repr__(self) -> str:
        return f'<Accountable_Concept: {self.code}>'

    def __str__(self) -> str:
        return self.code
