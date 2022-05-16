from django.forms import ModelForm, modelformset_factory

from adin.core.forms import GenericCreateForm, GenericDeleteForm, GenericActivateForm
from accountables.models import Accountable_Transaction_Type

class Transaction_TypeCreateModelForm(GenericCreateForm):

    pk_name = 'name'

    class Meta:
        model = Accountable_Transaction_Type
        fields = ['name']

    def clean_name(self):
        return self.clean_pk()

class Transaction_TypeDetailModelForm(ModelForm):

    class Meta:
        model = Accountable_Transaction_Type
        fields = ['state', 'name']

class Transaction_TypeDeleteModelForm(GenericDeleteForm):

    class Meta:
        model = Accountable_Transaction_Type
        fields = ['name']

class Transaction_TypeActivateModelForm(GenericActivateForm):

    class Meta:
        model = Accountable_Transaction_Type
        fields = ['name']

Transaction_TypeListModelFormSet = modelformset_factory(Accountable_Transaction_Type, fields=('state', 'name',), extra=0)

Transaction_TypeModelFormSet = modelformset_factory(Accountable_Transaction_Type, fields=('name', ), extra=0)
