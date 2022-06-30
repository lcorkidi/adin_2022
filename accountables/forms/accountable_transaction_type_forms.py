from django.forms import Form, ModelChoiceField, Select, ModelForm, modelformset_factory

from adin.core.forms import GenericCreateForm, GenericDeleteForm, GenericActivateForm
from accountables.models import Accountable, Accountable_Transaction_Type


class Accountable_Transaction_TypeCreateModelForm(GenericCreateForm):

    pk_name = 'name'

    class Meta:
        model = Accountable_Transaction_Type
        fields = ['name']

    def clean_name(self):
        return self.clean_pk()

class Accountable_Transaction_TypeDetailModelForm(ModelForm):

    class Meta:
        model = Accountable_Transaction_Type
        fields = ['state', 'name']

class Accountable_Transaction_TypeDeleteModelForm(GenericDeleteForm):

    class Meta:
        model = Accountable_Transaction_Type
        fields = ['name']

class Accountable_Transaction_TypeActivateModelForm(GenericActivateForm):

    class Meta:
        model = Accountable_Transaction_Type
        fields = ['name']

class Accountable_Transaction_TypeAddForm(Form):

    accountable = ModelChoiceField(
        queryset=Accountable.active.all(),
        widget=Select(attrs={'readonly':True}),
        label='Contrato de Arriendo Inmueble'
    )
    transaction_type = ModelChoiceField(
        queryset=Accountable_Transaction_Type.active.all(),
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

class Accountable_Transaction_TypeRemoveForm(Form):

    accountable = ModelChoiceField(
        queryset=Accountable.active.all(),
        label='Contrato de Arriendo Inmueble'
    )
    transaction_type = ModelChoiceField(
        queryset=Accountable_Transaction_Type.active.all(),
        label='Concepto Cargo'
    )

    def clean(self):
        if self.has_changed():
            msg = f'Información inmutable del objeto ha cambiado.'
            self.add_error(None, msg)
        return super().clean()

    def remove(self):
        cleaned_data = self.cleaned_data
        accountable = cleaned_data.get('accountable')
        transaction_type = cleaned_data.get('transaction_type')
        accountable.transaction_types.remove(transaction_type)

Accountable_Transaction_TypeListModelFormSet = modelformset_factory(Accountable_Transaction_Type, fields=('state', 'name',), extra=0)

Accountable_Transaction_TypeModelFormSet = modelformset_factory(Accountable_Transaction_Type, fields=('name', ), extra=0)
