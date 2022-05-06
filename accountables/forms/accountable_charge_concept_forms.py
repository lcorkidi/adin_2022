from django.forms import Form, ChoiceField, ValidationError

from accounting.models import Charge_Concept
from accounting.utils import chacon2code

class Accountable_Charge_ConceptCreateForm(Form):

    transaction_type = ChoiceField(
        choices=(),
        label='Tipo de Cargo'
    )
    date = ChoiceField(
        choices=(),
        label='Fecha Cargo'
    )
    
    def __init__(self, obj, *args, **kwargs):
        field_choices = {
            'transaction_type': [(list(obj.transaction_types.all()).index(item), item) for item in list(obj.transaction_types.all())],
            'date': [(obj.subclass_obj().pending_charge_concept_dates().index(item), item) for item in obj.subclass_obj().pending_charge_concept_dates()]
        }
        super(Accountable_Charge_ConceptCreateForm, self).__init__(*args, **kwargs)
        self.fields['transaction_type'].choices = field_choices['transaction_type']
        self.fields['date'].choices = field_choices['date']

    def clean(self):
        transaction_type = self.cleaned_data.get('transaction_type')
        date = self.cleaned_data.get('date')
        transaction_types = {str(list(self.accountable.transaction_types.all()).index(item)): item for item in list(self.accountable.transaction_types.all())}
        dates = {str(self.accountable.subclass_obj().pending_charge_concept_dates().index(item)): item for item in self.accountable.subclass_obj().pending_charge_concept_dates()}
        obj = Charge_Concept(
            accountable=self.accountable,
            transaction_type=transaction_types[transaction_type],
            date=dates[date],
        )
        code = chacon2code(obj)
        if Charge_Concept.objects.filter(pk=code).exists():
            obj = Charge_Concept.objects.get(pk=code)
            if obj.state == 0:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con estos datos ya existe y está inactiva.")
            else:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con estos datos ya existe.")
        return super().clean()

    def save(self):
        transaction_type = self.cleaned_data.get('transaction_type')
        date = self.cleaned_data.get('date')
        transaction_types = {str(list(self.accountable.transaction_types.all()).index(item)): item for item in list(self.accountable.transaction_types.all())}
        dates = {str(self.accountable.subclass_obj().pending_charge_concept_dates().index(item)): item for item in self.accountable.subclass_obj().pending_charge_concept_dates()}
        self.accountable = Charge_Concept(
            accountable=self.accountable,
            transaction_type=transaction_types[transaction_type],
            date=dates[date],
            state_change_user=self.creator
        )
        self.accountable.save()

class Accountable_Charge_ConceptDeleteForm(Form):
    pass

class Accountable_Charge_ConceptActivateForm(Form):
    pass

