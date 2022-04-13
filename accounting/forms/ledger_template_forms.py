from django.forms import ModelForm, modelformset_factory

from adin.core.forms import GenericCreateForm
from accounting.models import Ledger_Template

class Ledger_TemplateCreateModelForm(GenericCreateForm):

    class Meta:
        model = Ledger_Template
        fields = ['transaction_type', 'ledger_type']

class Ledger_TemplateDetailModelForm(ModelForm):

    class Meta:
        model = Ledger_Template
        fields = ['transaction_type', 'ledger_type']

class Ledger_TemplateDeleteModelForm(ModelForm):

    class Meta:
        model = Ledger_Template
        fields = ['transaction_type', 'ledger_type']

Ledger_TemplateListModelFormSet = modelformset_factory(Ledger_Template, fields=('transaction_type', 'ledger_type'), extra=0)
