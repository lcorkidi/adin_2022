import pandas as pd
from django.db import models
from django.db.models import Sum
from django.contrib.contenttypes.models import ContentType

from adin.core.models import BaseModel
from adin.utils.data_check import errors_report
from accountables.utils.models_func import accon_2_code
from accountables.utils.accounting_data import ACCOUNT_RECEIPT_PRIORITY

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
        'accountables.Transaction_Type',
        through='Accountable_Transaction_Type',
        through_fields=('accountable', 'transaction_type'),
        related_name='accountable',
        related_query_name='accountables',
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

class Accountable_Transaction_TypeFinderManager(models.Manager):
    def from_related(self, obj1, obj2):
        base_args = {}
        if isinstance(obj1, Accountable):
            base_args['lease'] = obj1
            base_args['person'] = obj2
        else:
            base_args['lease'] = obj2
            base_args['person'] = obj1
        return self.get_queryset().get(**base_args)

    def get_queryset(self):
        return super().get_queryset()

class Accountable_Transaction_Type(BaseModel):

    accountable = models.ForeignKey(
        Accountable,
        on_delete=models.PROTECT,
        related_name='accountable_transaction_type',
        related_query_name='accountable_transaction_types',
        verbose_name='Contabilizable'
    )
    transaction_type = models.ForeignKey(
        'accountables.Transaction_Type',
        on_delete=models.PROTECT,
        related_name='accountable_transaction_type',
        related_query_name='accountable_transaction_types',
        verbose_name='Tipo Transacción'
    )
    commit_template = models.ForeignKey(
        'accounting.Ledger_Template',
        on_delete=models.PROTECT,
        related_name='accountable_transaction_type_commit',
        related_query_name='accountable_transaction_type_commits',
        verbose_name='Formato Causacion'
    )
    bill_template = models.ForeignKey(
        'accounting.Ledger_Template',
        on_delete=models.PROTECT,
        related_name='accountable_transaction_type_bill',
        related_query_name='accountable_transaction_type_bill',
        verbose_name='Formato Facturacion'
    )
    receive_template = models.ForeignKey(
        'accounting.Ledger_Template',
        on_delete=models.PROTECT,
        related_name='accountable_transaction_type_receive',
        related_query_name='accountable_transaction_type_receive',
        verbose_name='Formato Ingreso'
    )

    objects = models.Manager()
    find = Accountable_Transaction_TypeFinderManager()

    class Meta:
        app_label = 'accountables'
        verbose_name = 'Transacción Tipo Contabilizable'
        verbose_name_plural = 'Transacciones Tipo Contabilizables'
        permissions = [
            ('activateaccountable__transaction_type', 'Can activate accountable transaction type.'),
            ('checkaccountable__transaction_type', 'Can check accountable transaction type.'),
        ]

    def __repr__(self) -> str:
        return f'<Accountable_Transaction_Type: {self.accountable}_{self.transaction_type}>'

    def __str__(self) -> str:
        return f'{self.accountable}_{self.transaction_type}'

class Transaction_Type(BaseModel):

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
            ('check_transaction_type', 'Can check transaction type.'),
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
        return f'<Transaction_Type: {self.name}>'
    
    def __str__(self) -> str:
        return self.name

class Accountable_ConceptPendingManager(models.Manager):

    def commit(self):
        qs = self.get_queryset()
        objs_df = pd.DataFrame(qs.values('code', 'date'))
        sorted_objs_df = objs_df.sort_values(by=['date']).assign(acc_con=objs_df.code.apply(lambda x: Accountable_Concept.objects.get(pk=x)))
        referenced_objs_df = sorted_objs_df.assign(pending=sorted_objs_df.acc_con.apply(lambda x: x.Pending_Ledger(x.accountable.accountable_transaction_type.get(transaction_type=x.transaction_type).commit_template)))
        objs_list = referenced_objs_df[referenced_objs_df['pending']==True]['code'].to_list()
        return qs.filter(code__in=objs_list)

    def bill(self):
        qs = self.get_queryset()
        code_df = pd.DataFrame(qs.values('code'))
        obj_df = code_df.assign(acc_con=code_df.code.apply(lambda x: Accountable_Concept.objects.get(pk=x)))
        pre_pen_df = obj_df.assign(
                                not_bil=obj_df.acc_con.apply(lambda x: x.Pending_Ledger(x.accountable.accountable_transaction_type.get(transaction_type=x.transaction_type).bill_template)),
                                pre_exi=obj_df.acc_con.apply(lambda x: x.accountable.accountable_concept.exclude(state=0).filter(date__lt=x.date).exists()),
                                bil_eli=obj_df.apply(lambda x: x.acc_con.accountable.accountable_concept.exclude(state=0).filter(date__lt=x.acc_con.date).latest('date').ReceivableDueNone(ACCOUNT_RECEIPT_PRIORITY) if x.acc_con.accountable.accountable_concept.exclude(state=0).filter(date__lt=x.acc_con.date).exists() else False, axis=1)
                            )
        pen_bil_df = pre_pen_df.assign(bil_pen=pre_pen_df.apply(lambda x: True if x.not_bil and (not x.pre_exi or (x.pre_exi and x.bil_eli)) else False, axis=1))
        objs_list = pen_bil_df[pen_bil_df['bil_pen']==True]['code'].to_list()
        return qs.filter(code__in=objs_list)

    def ledger_type_dict(self, typ_abr):
        if typ_abr == 'CA':
            qs = self.commit()
        elif typ_abr == 'FV':
            qs = self.bill()
        else:
            return
        code_df = pd.DataFrame(qs.values('code'))
        obj_df = code_df.assign(accountable_concept=code_df.code.apply(lambda x: self.get_queryset().get(pk=x)))
        return obj_df.assign(
                        ledger_template=obj_df.accountable_concept.apply(lambda x: x.accountable.accountable_transaction_type.get(transaction_type__name='Canon Mensual Arriendo Inmueble').commit_template),
                        ledger_type=obj_df.accountable_concept.apply(lambda x: x.accountable.accountable_transaction_type.get(transaction_type__name='Canon Mensual Arriendo Inmueble').commit_template.ledger_type),
                        accountable=obj_df.accountable_concept.apply(lambda x: x.accountable),
                        holder=obj_df.accountable_concept.apply(lambda x: x.accountable.ledger_holder()),
                        third_party=obj_df.accountable_concept.apply(lambda x: x.accountable.ledger_third_party()),
                        concept_date=obj_df.accountable_concept.apply(lambda x: x.date),
                        concept_value=obj_df.accountable_concept.apply(lambda x: x.value)
                    ).drop(['code'], axis=1).to_dict('records')

    def ledger(self, acc, led_tem):
        qs = self.get_queryset().filter(accountable=acc)
        objs_df = pd.DataFrame(qs.values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)
        pending_charge_df=objs_df.assign(pending_charge=objs_df.code.apply(lambda x: qs.get(pk=x).Pending_Ledger(led_tem)))
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
        Transaction_Type,
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

    def Pending_Ledger(self, led_tem):
        from accounting.models import Charge

        for cha_tem in led_tem.charges_templates.all():
            if not Charge.objects.exclude(state=0).filter(
                account=cha_tem.account,
                value=cha_tem.factor.factored_value(self.accountable, self.date, self.value, cha_tem.nature),
                concept=self
            ).exists():
                return True
        return False

    def ReceivableDueAll(self, account_priority):
        from accounting.models import Charge

        return False if Charge.objects.exclude(state=0).filter(account__in=[account for account in account_priority.keys()], concept=self, value__lt=0, ledger__type__abreviation='RC').exists() else True

    def ReceivableDueSome(self, account_priority):
        from accounting.models import Charge

        receivable = abs(Charge.objects.exclude(state=0).filter(account__in=[account for account in account_priority.keys()], concept=self, value__gt=0, ledger__type__abreviation='FV').aggregate(receivable=Sum('value'))['receivable']) if Charge.objects.exclude(state=0).filter(account__in=[account for account in account_priority.keys()], concept=self, value__gt=0, ledger__type__abreviation='FV').exists() else 0
        received = abs(Charge.objects.exclude(state=0).filter(account__in=[account for account in account_priority.keys()], concept=self, value__lt=0, ledger__type__abreviation='RC').aggregate(received=Sum('value'))['received']) if Charge.objects.exclude(state=0).filter(account__in=[account for account in account_priority.keys()], concept=self, value__lt=0, ledger__type__abreviation='RC').exists() else 0

        return True if received > 0 and receivable - received > 0 else False

    def ReceivableDueNone(self, account_priority):
        from accounting.models import Charge

        receivable = abs(Charge.objects.exclude(state=0).filter(account__in=[account for account in account_priority.keys()], concept=self, value__gt=0, ledger__type__abreviation='FV').aggregate(receivable=Sum('value'))['receivable']) if Charge.objects.exclude(state=0).filter(account__in=[account for account in account_priority.keys()], concept=self, value__gt=0, ledger__type__abreviation='FV').exists() else 0
        received = abs(Charge.objects.exclude(state=0).filter(account__in=[account for account in account_priority.keys()], concept=self, value__lt=0, ledger__type__abreviation='RC').aggregate(received=Sum('value'))['received']) if Charge.objects.exclude(state=0).filter(account__in=[account for account in account_priority.keys()], concept=self, value__lt=0, ledger__type__abreviation='RC').exists() else 0

        return True if receivable > 0 and receivable - received == 0 else False

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
