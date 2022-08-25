from django.forms import Form, ChoiceField, ModelChoiceField, IntegerField, DateField, ValidationError, BaseFormSet, modelformset_factory, formset_factory

from adin.core.forms import GenericActivateRelatedForm, GenericDeleteRelatedForm
from accountables.models import Accountable_Concept, Accountable_Transaction_Type, Accountable

class Accountable_ConceptCreateForm(Form):

    accountable = ModelChoiceField(
        queryset=Accountable.objects.exclude(state=0),
        empty_label=None,
        label='Contabilizable'
    )
    transaction_type = ModelChoiceField(
        queryset=Accountable_Transaction_Type.objects.exclude(state=0),
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
        accountable = self.cleaned_data.get('accountable')
        if not accountable.start_date:
            raise ValidationError(f"{accountable} no tiene fecha de ocupación.")
        else:
            if date < accountable.start_date:
                self.add_error('date', f'{date} es anterior a fecha de ocupación de {accountable}.')
        if accountable.end_date and date > accountable.end_date:
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
        queryset=Accountable_Transaction_Type.objects.exclude(state=0),
        empty_label=None,
        label='Tipo de Transacción'
    )
    date = DateField(
        disabled=True,
        label='Fecha Cargo'
    )
    value = IntegerField(
        label='Valor'
    )
    
    def __init__(self, *args, accountable, **kwargs):
        super(Accountable_ConceptPendingCreateForm, self).__init__(*args, **kwargs)
        self.fields['transaction_type'].queryset = accountable.transaction_types.exclude(state=0)

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
        Accountable_Concept(
            state_change_user=creator,
            accountable = self.initial['accountable'],
            transaction_type = self.cleaned_data['transaction_type'],
            date = self.cleaned_data['date'],
            value = self.cleaned_data['value']
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

class Accountable_ConceptPendingCreateBseFormSet(BaseFormSet):

    def save(self):
        for form in self.forms:
            form.save(self.creator)

Accountable_ConceptModelFormSet = modelformset_factory(Accountable_Concept, fields=('state', 'transaction_type', 'date', 'value'), extra=0)

Accountable_ConceptPendingFormSet = formset_factory(Accountable_ConceptPendingCreateForm, formset=Accountable_ConceptPendingCreateBseFormSet, extra=0)
