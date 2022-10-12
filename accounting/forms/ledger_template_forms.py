from django.forms import Form, ModelForm, ModelChoiceField, modelformset_factory
from django.contrib.contenttypes.models import ContentType

from adin.core.forms import GenericCreateForm
from accounting.models import Ledger_Template
from accountables.models import Accountable

class Ledger_TemplateCreateModelForm(GenericCreateForm):

    accountable_class = ModelChoiceField(
        queryset=ContentType.objects.filter(model__in=['lease_realty']),
        label='Clase Contabilizable'
    )

    class Meta:
        model = Ledger_Template
        fields = ['transaction_type', 'ledger_type', 'accountable_class']

    def save(self, creator_user, *args, **kwargs):
        base_args = {}
        base_args['accountable_class'] = self.cleaned_data.get('accountable_class')
        base_args['ledger_type'] = self.cleaned_data.get('ledger_type')
        base_args['transaction_type'] = self.cleaned_data.get('transaction_type')
        base_args['state_change_user'] = creator_user
        ledger_template = Ledger_Template(**base_args)
        ledger_template.save()
        return ledger_template

class Ledger_TemplateDetailModelForm(ModelForm):

    class Meta:
        model = Ledger_Template
        fields = ['transaction_type', 'ledger_type', 'accountable_class']

class Ledger_TemplateDeleteModelForm(ModelForm):

    class Meta:
        model = Ledger_Template
        fields = ['transaction_type', 'ledger_type', 'accountable_class']

class Ledger_TemplateSelectForm(Form):

    ledger_template = ModelChoiceField(
        queryset=Ledger_Template.objects.exclude(state=0),
        label='Formato Registro'
    )

class Ledger_TemplateSelectAccountableForm(Form):

    ledger_template = ModelChoiceField(
        queryset=Ledger_Template.objects.exclude(state=0),
        label='Formato Registro'
    )
    accountable = ModelChoiceField(
        queryset=Accountable.objects.exclude(state=0),
        label='Contabilizable'
    )
    
    def __init__(self, *args, **kwargs):
        obj=kwargs['initial']['ledger_template']
        field_choices = {
            'accountable': obj.accountable_class.model_class().__bases__[0].objects.filter(code__in=obj.accountable_class.model_class().active.values_list('code', flat=True))
        }
        super(Ledger_TemplateSelectAccountableForm, self).__init__(*args, **kwargs)
        self.fields['accountable'].queryset = field_choices['accountable']

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

    def has_concept(self):
        accountable = self.cleaned_data.get('accountable')
        return accountable.accountable_concept.exclude(state=0).exists()

Ledger_TemplateListModelFormSet = modelformset_factory(Ledger_Template, fields=('transaction_type', 'ledger_type', 'accountable_class'), extra=0)

Ledger_TemplateAvailableModelFormset = modelformset_factory(Ledger_Template, fields=('code', ), extra=0)
