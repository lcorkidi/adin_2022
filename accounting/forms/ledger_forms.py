from django.forms import ModelForm, modelformset_factory

from adin.core.forms import GenericCreateForm, GenericDeleteForm, GenericActivateForm
from adin.core.widgets import SelectDateSpanishWidget
from accounting.models import Ledger

class LedgerCreateModelForm(GenericCreateForm):

    class Meta:
        model = Ledger
        fields = ['type', 'holder', 'third_party', 'date', 'description']
        widgets = {
            'date': SelectDateSpanishWidget()
        }

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

class LedgerDetailModelForm(ModelForm):

    class Meta:
        model = Ledger
        fields = ['state', 'code', 'holder', 'third_party', 'date', 'description']

class LedgerDeleteModelForm(GenericDeleteForm):

    exclude_fields = ['charge']

    class Meta:
        model = Ledger
        fields = ['code', 'holder', 'third_party', 'date', 'description']

class LedgerActivateModelForm(GenericActivateForm):

    class Meta:
        model = Ledger
        fields = ['code', 'holder', 'third_party', 'date', 'description']

LedgerListModelFormSet = modelformset_factory(Ledger, fields=('state', 'code', 'holder', 'third_party', 'date'), extra=0)
