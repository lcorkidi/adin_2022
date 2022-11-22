import datetime as dt
from django.forms import Form, ChoiceField, ModelChoiceField, IntegerField, DateField, ModelForm, ValidationError, BaseFormSet, BaseModelFormSet, modelformset_factory, formset_factory

from adin.core.forms import GenericActivateRelatedForm, GenericDeleteRelatedForm
from accountables.models import Accountable_Concept, Transaction_Type, Accountable
from accountables.utils.accounting_data import ACCOUNT_RECEIPT_PRIORITY

class Accountable_ConceptCreateSelectTransaction_TypeForm(Form):

    accountable = ModelChoiceField(
        queryset=Accountable.objects.exclude(state=0),
        empty_label=None,
        label='Contabilizable'
    )
    transaction_type = ModelChoiceField(
        queryset=Transaction_Type.objects.exclude(state=0),
        empty_label=None,
        label='Tipo de Transacción'
    )
    
    def __init__(self, obj, *args, **kwargs):
        field_choices = {
            'transaction_type': obj.transaction_types.exclude(state=0),
        }
        super(Accountable_ConceptCreateSelectTransaction_TypeForm, self).__init__(*args, **kwargs)
        self.fields['transaction_type'].queryset = field_choices['transaction_type']

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

class Accountable_ConceptCreateForm(Form):

    accountable = ModelChoiceField(
        queryset=Accountable.objects.exclude(state=0),
        empty_label=None,
        label='Contabilizable'
    )
    transaction_type = ModelChoiceField(
        queryset=Transaction_Type.objects.exclude(state=0),
        empty_label=None,
        label='Tipo de Transacción'
    )
    date = ChoiceField(
        choices=(),
        label='Fecha Cargo'
    )
    value = IntegerField(
        label='Valor'
    )
    
    def __init__(self, obj, *args, **kwargs):
        field_choices = {
            'transaction_type': obj.transaction_types.exclude(state=0),
            'date': [(item,item) for item in obj.subclass_obj().pending_concept_dates()]
        }
        super(Accountable_ConceptCreateForm, self).__init__(*args, **kwargs)
        self.fields['transaction_type'].queryset = field_choices['transaction_type']
        self.fields['date'].choices = field_choices['date']

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

    def clean_transaction_type(self):
        transaction_type = self.cleaned_data.get('transaction_type')
        accountable = self.cleaned_data.get('accountable')
        if transaction_type not in accountable.transaction_types.exclude(state=0):
            self.add_error('transaction_type', f'{transaction_type} no una opcion de tipo de transacción de {accountable}.')
        return transaction_type

    def clean_date(self):
        date = self.cleaned_data.get('date')
        date = dt.date(int(date.split('-')[0]), int(date.split('-')[1]), int(date.split('-')[2]))
        accountable = self.cleaned_data.get('accountable')
        if not accountable.subclass_obj().start_date:
            raise ValidationError(f"{accountable} no tiene fecha de ocupación.")
        else:
            if date < accountable.subclass_obj().start_date:
                self.add_error('date', f'{date} es anterior a fecha de ocupación de {accountable}.')
        if accountable.subclass_obj().end_date and date > accountable.subclass_obj().end_date:
            self.add_error('date', f'{date} es posterior a fecha de terminación de {accountable}.')
        if date not in accountable.subclass_obj().pending_concept_dates():
            self.add_error('date', f'{date} no una opcion de disponible para {accountable}.')
        return date

    def clean(self):
        cleaned_data = self.cleaned_data
        if Accountable_Concept.objects.filter(accountable=cleaned_data['accountable'],
                transaction_type=cleaned_data['transaction_type'],
                date=cleaned_data['date']
                ).exists():
            obj = Accountable_Concept.objects.get(accountable=cleaned_data['accountable'],
                transaction_type=cleaned_data['transaction_type'],
                date=cleaned_data['date'])
            if obj.state == 0:
                raise ValidationError(f"{obj._meta.model._meta.verbose_name} con estos datos ya existe y está inactiva.")
            else:
                raise ValidationError(f"{obj._meta.model._meta.verbose_name} con estos datos ya existe.")
        return super().clean()

    def save(self, user):
        cleaned_data = self.cleaned_data
        acc_con = Accountable_Concept(
            accountable=cleaned_data['accountable'],
            transaction_type=cleaned_data['transaction_type'],
            date=cleaned_data['date'],
            value=cleaned_data['value'],
            state_change_user=user)
        acc_con.save()

class Accountable_ConceptPendingCreateForm(Form):

    transaction_type = ModelChoiceField(
        queryset=Transaction_Type.objects.exclude(state=0),
        empty_label=None,
        disabled=True,
        label='Tipo de Transacción'
    )
    date = DateField(
        disabled=True,
        label='Fecha Cargo'
    )
    value = IntegerField(
        disabled=True,
        label='Valor'
    )

    def clean_transaction_type(self):
        transaction_type = self.cleaned_data.get('transaction_type')
        accountable = self.initial['accountable']
        if transaction_type not in accountable.transaction_types.exclude(state=0):
            self.add_error('transaction_type', f'{transaction_type} no una opcion de tipo de transacción de {accountable}.')
        return transaction_type

    def clean(self):
        cleaned_data = self.cleaned_data
        if Accountable_Concept.objects.filter(accountable = self.initial['accountable'],
                transaction_type = cleaned_data['transaction_type'],
                date = cleaned_data['date']
                ).exists():
            obj = Accountable_Concept.objects.get(accountable = self.initial['accountable'],
                transaction_type = cleaned_data['transaction_type'],
                date = cleaned_data['date']
                )
            if obj.state == 0:
                raise ValidationError(f"{obj._meta.model._meta.verbose_name} con estos datos ya existe y está inactiva.")
            else:
                raise ValidationError(f"{obj._meta.model._meta.verbose_name} con estos datos ya existe.")
        return super().clean()

    def save(self, creator):
        acc = self.initial['accountable']
        dt = self.cleaned_data['date']
        Accountable_Concept(
            state_change_user=creator,
            accountable = acc,
            transaction_type = self.cleaned_data['transaction_type'],
            date = dt,
            value = self.cleaned_data['value'],
            value_relation=acc.date_value.earliest('date') if dt < acc.subclass_obj().doc_date else acc.date_value.exclude(date__gt=dt).latest('date')
        ).save()

class Accountable_ConceptDeleteForm(GenericDeleteRelatedForm):

    class Meta:
        model = Accountable_Concept
        exclude = ('state',)

    def save(self, user):
        accon = self.instance
        accon.state = 0
        accon.state_change_user = user
        accon.save()        

class Accountable_ConceptActivateForm(GenericActivateRelatedForm):

    class Meta:
        model = Accountable_Concept
        exclude = ('state',)

    def save(self, user):
        accon = self.instance
        accon.state = 2
        accon.state_change_user = user
        accon.save()        

class Accountable_ConceptPendingCreateBaseFormSet(BaseFormSet):

    def save(self):
        for form in self.forms:
            form.save(self.creator)

class Accountable_ConceptRelatedModelForm(ModelForm):

    def add_errors(self):
        actions_on = []
        acc_con = self.instance
        com_tem = acc_con.get_applicable_ledger_template(acc_con.transaction_type, 'CA', acc_con.date)
        if self.instance.Pending_Ledger(com_tem):
            actions_on.append('commit')
        else:
            bil_tem = acc_con.get_applicable_ledger_template(acc_con.transaction_type, 'CA', acc_con.date)
            if self.instance.Pending_Ledger(bil_tem):
                if acc_con.accountable.accountable_concept.exclude(state=0).filter(date__lt=acc_con.date).exists():
                    pre_acc_con = acc_con.accountable.accountable_concept.exclude(state=0).filter(date__lt=acc_con.date).latest('date')
                    if pre_acc_con.ReceivableDueNone(ACCOUNT_RECEIPT_PRIORITY):
                        actions_on.append('bill')
                else:
                    actions_on.append('bill')
            else:
                if acc_con.accountable.accountable_concept.exclude(state=0).filter(date__lt=acc_con.date).exists():
                    pre_acc_con = acc_con.accountable.accountable_concept.exclude(state=0).filter(date__lt=acc_con.date).latest('date')
                    if acc_con.ReceivableDueAll(ACCOUNT_RECEIPT_PRIORITY) and pre_acc_con.ReceivableDueNone(ACCOUNT_RECEIPT_PRIORITY):
                        actions_on.append('receipt')
                elif acc_con.ReceivableDueAll(ACCOUNT_RECEIPT_PRIORITY):
                    actions_on.append('receipt')

        if actions_on:
            self.actions_on = actions_on

class Accountable_ConceptRelatedBaseModelFormSet(BaseModelFormSet):

    def __init__(self, rel_pk, *args, **kwargs):
        super(Accountable_ConceptRelatedBaseModelFormSet, self).__init__(*args, **kwargs)
        self.add_errors(rel_pk)

    def add_errors(self, rel_pk):
        obj = Accountable.objects.get(pk=rel_pk)
        formset_errors = []
        if obj.transaction_types.filter(name='Canon Mensual Arriendo Inmueble').exists():
            tra_typ = Transaction_Type.objects.get(name='Canon Mensual Arriendo Inmueble')
            if obj.pending_concept_date_values(tra_typ):
                formset_errors.append(f'FECHA y VALOR pendientes para conceptos tipo {tra_typ.name.upper()}: {obj.pending_concept_date_values(tra_typ)}')
        if formset_errors:
            self.formset_errors = formset_errors
        for form in self.forms:
            form.add_errors()

Accountable_ConceptModelFormSet = modelformset_factory(Accountable_Concept, form=Accountable_ConceptRelatedModelForm, formset=Accountable_ConceptRelatedBaseModelFormSet, fields=('state', 'transaction_type', 'date', 'value'), extra=0)

Accountable_ConceptPendingFormSet = formset_factory(Accountable_ConceptPendingCreateForm, formset=Accountable_ConceptPendingCreateBaseFormSet, extra=0)

class Accountable_ConceptPendingBulkCreateForm(Form):

    accountable = ModelChoiceField(
        queryset=Accountable.objects.exclude(state=0),
        disabled=True,
        label='Contabilizable'
    )
    transaction_type = ModelChoiceField(
        queryset=Transaction_Type.objects.exclude(state=0),
        disabled=True,
        label='Tipo de Transacción'
    )
    date = DateField(
        disabled=True,
        label='Fecha Cargo'
    )
    value = IntegerField(
        disabled=True,
        label='Valor'
    )

    def clean_transaction_type(self):
        transaction_type = self.cleaned_data.get('transaction_type')
        accountable = self.initial['accountable']
        if transaction_type not in accountable.transaction_types.exclude(state=0):
            self.add_error('transaction_type', f'{transaction_type} no una opcion de tipo de transacción de {accountable}.')
        return transaction_type

    def clean(self):
        cleaned_data = self.cleaned_data
        if Accountable_Concept.objects.filter(accountable = self.initial['accountable'],
                transaction_type = cleaned_data['transaction_type'],
                date = cleaned_data['date']
                ).exists():
            obj = Accountable_Concept.objects.get(accountable = self.initial['accountable'],
                transaction_type = cleaned_data['transaction_type'],
                date = cleaned_data['date']
                )
            if obj.state == 0:
                raise ValidationError(f"{obj._meta.model._meta.verbose_name} con estos datos ya existe y está inactiva.")
            else:
                raise ValidationError(f"{obj._meta.model._meta.verbose_name} con estos datos ya existe.")
        return super().clean()

    def save(self, creator):
        acc = self.initial['accountable']
        dt = self.cleaned_data['date']
        Accountable_Concept(
            state_change_user=creator,
            accountable = acc,
            transaction_type = self.cleaned_data['transaction_type'],
            date = dt,
            value = self.cleaned_data['value'],
            value_relation=acc.date_value.earliest('date') if dt < acc.subclass_obj().doc_date else acc.date_value.exclude(date__gt=dt).latest('date')
        ).save()

Accountable_ConceptPendingBulkFormSet = formset_factory(Accountable_ConceptPendingBulkCreateForm, formset=Accountable_ConceptPendingCreateBaseFormSet, extra=0)

Accountable_ConceptPendingLedgerBulkFormSet = modelformset_factory(Accountable_Concept, fields=('accountable', 'transaction_type', 'date', 'value'), extra=0)
