from django.forms import Form, ChoiceField, ModelChoiceField, IntegerField, DateField, ValidationError, BaseFormSet, modelformset_factory, formset_factory

from accountables.models import Accountable_Concept, Accountable_Transaction_Type, Accountable
from accountables.utils import acc_con2code

class Accountable_ConceptCreateForm(Form):

    transaction_type = ChoiceField(
        choices=(),
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
            'transaction_type': [(list(obj.transaction_types.exclude(state=0)).index(item), item) for item in list(obj.transaction_types.exclude(state=0))],
            'date': [(obj.subclass_obj().pending_accountable_concept_dates().index(item), item) for item in obj.subclass_obj().pending_accountable_concept_dates()]
        }
        super(Accountable_ConceptCreateForm, self).__init__(*args, **kwargs)
        self.fields['transaction_type'].choices = field_choices['transaction_type']
        self.fields['date'].choices = field_choices['date']

    def clean(self):
        transaction_type = self.cleaned_data.get('transaction_type')
        date = self.cleaned_data.get('date')
        transaction_types = {str(list(self.accountable.transaction_types.exclude(state=0)).index(item)): item for item in list(self.accountable.transaction_types.exclude(state=0))}
        dates = {str(self.accountable.subclass_obj().pending_accountable_concept_dates().index(item)): item for item in self.accountable.subclass_obj().pending_accountable_concept_dates()}
        obj = Accountable_Concept(
            accountable=self.accountable,
            transaction_type=transaction_types[transaction_type],
            date=dates[date],
        )
        code = acc_con2code(obj)
        if Accountable_Concept.objects.filter(pk=code).exists():
            obj = Accountable_Concept.objects.get(pk=code)
            if obj.state == 0:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con estos datos ya existe y está inactiva.")
            else:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con estos datos ya existe.")
        return super().clean()

    def save(self):
        transaction_type = self.cleaned_data.get('transaction_type')
        date = self.cleaned_data.get('date')
        transaction_types = {str(list(self.accountable.transaction_types.exclude(state=0)).index(item)): item for item in list(self.accountable.transaction_types.exclude(state=0))}
        dates = {str(self.accountable.subclass_obj().pending_charge_concept_dates().index(item)): item for item in self.accountable.subclass_obj().pending_charge_concept_dates()}
        self.accountable = Accountable_Concept(
            accountable=self.accountable,
            transaction_type=transaction_types[transaction_type],
            date=dates[date],
            state_change_user=self.creator
        )
        self.accountable.save()

class Accountable_ConceptPendingCreateForm(Form):

    transaction_type = ModelChoiceField(
        queryset=Accountable_Transaction_Type.objects.exclude(state=0),
        label='Tipo de Transacción'
    )
    date = DateField(
        label='Fecha Cargo'
    )
    value = IntegerField(
        label='Valor'
    )

    def clean_transaction_type(self):
        transaction_type = self.cleaned_data.get('transaction_type')
        accountable = self.initial['accountable']
        if transaction_type not in accountable.transaction_types.exclude(state=0):
            self.add_error('transaction_type', f'{transaction_type} no una opcion de topi de transacción de {accountable}.')
        return transaction_type

    def save(self, creator):
        Accountable_Concept(
            state_change_user=creator,
            accountable = self.initial['accountable'],
            transaction_type = self.cleaned_data['transaction_type'],
            date = self.cleaned_data['date'],
            value = self.cleaned_data['value']
        ).save()

class Accountable_ConceptDeleteForm(Form):
    pass

class Accountable_ConceptActivateForm(Form):
    pass

class Accountable_ConceptPendingCreateBseFormSet(BaseFormSet):

    def save(self):
        for form in self.forms:
            form.save(self.creator)

Accountable_ConceptModelFormSet = modelformset_factory(Accountable_Concept, fields=('state', 'transaction_type', 'date', 'value'), extra=0)

Accountable_ConceptPendingFormSet = formset_factory(Accountable_ConceptPendingCreateForm, formset=Accountable_ConceptPendingCreateBseFormSet, extra=0)
