from django.forms import Form, ModelChoiceField, Select

from accountables.models import Accountable
from references.models import Transaction_Type

class Lease_Realty_Transaction_TypeFrom(Form):

    accountable = ModelChoiceField(
        queryset=Accountable.active.all(),
        widget=Select(attrs={'readonly':True}),
        label='Contrato de Arriendo Inmueble'
    )
    transaction_type = ModelChoiceField(
        queryset=Transaction_Type.active.all(),
        widget=Select(attrs={'readonly':False}),
        label='Concepto Cargo'
    )

    def clean(self):
        cleaned_data = self.cleaned_data
        accountable = cleaned_data.get('accountable')
        transaction_type = cleaned_data.get('transaction_type')
        if accountable.subclass_obj().transaction_types.filter(name=transaction_type.name).exists():
            msg = f'{accountable} ya tiene {transaction_type} relacionado.'
            self.add_error(None, msg)
        return super().clean()

    def add(self):
        cleaned_data = self.cleaned_data
        accountable = cleaned_data.get('accountable')
        transaction_type = cleaned_data.get('transaction_type')
        accountable.subclass_obj().transaction_types.add(transaction_type)

    def remove(self):
        pass