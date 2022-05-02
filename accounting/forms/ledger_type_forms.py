from django.forms import ModelForm, modelformset_factory

from adin.core.forms import GenericCreateForm, GenericDeleteForm, GenericActivateForm
from accounting.models import Ledger_Type

class Ledger_TypeCreateModelForm(GenericCreateForm):

    pk_name = 'name'

    class Meta:
        model = Ledger_Type
        fields = ['name', 'abreviation']

    def clean_name(self):
        return self.clean_pk()

class Ledger_TypeDetailModelForm(ModelForm):

    class Meta:
        model = Ledger_Type
        fields = ['state', 'name', 'abreviation']

class Ledger_TypeDeleteModelForm(GenericDeleteForm):

    class Meta:
        model = Ledger_Type
        fields = ['name', 'abreviation']

class Ledger_TypeActivateModelForm(GenericActivateForm):

    class Meta:
        model = Ledger_Type
        fields = ['name', 'abreviation']

Ledger_TypeListModelFormSet = modelformset_factory(Ledger_Type, fields=('state', 'name', 'abreviation'), extra=0)
