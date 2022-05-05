from django.forms import Form, ModelChoiceField, Select, ChoiceField

from accountables.models import Accountable
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

    def save(self):
        pass

class Accountable_Charge_ConceptDeleteForm(Form):
    pass

class Accountable_Charge_ConceptActivateForm(Form):
    pass

