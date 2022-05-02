from django.forms import ModelForm, ModelChoiceField, modelformset_factory
from django.contrib.contenttypes.models import ContentType

from adin.core.forms import GenericCreateForm
from accounting.models import Ledger_Template

class Ledger_TemplateCreateModelForm(GenericCreateForm):

    accountable_class = ModelChoiceField(
        queryset=ContentType.objects.filter(model__in=['lease_realty']),
        label='Clase Contabilizable'
    )

    class Meta:
        model = Ledger_Template
        fields = ['transaction_type', 'ledger_type', 'accountable_class']

class Ledger_TemplateDetailModelForm(ModelForm):

    class Meta:
        model = Ledger_Template
        fields = ['transaction_type', 'ledger_type', 'accountable_class']

class Ledger_TemplateDeleteModelForm(ModelForm):

    class Meta:
        model = Ledger_Template
        fields = ['transaction_type', 'ledger_type', 'accountable_class']

Ledger_TemplateListModelFormSet = modelformset_factory(Ledger_Template, fields=('transaction_type', 'ledger_type', 'accountable_class'), extra=0)
