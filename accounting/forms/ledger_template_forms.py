import datetime
from django.forms import Form, ModelForm, ModelChoiceField, DateField, IntegerField, ValidationError, BaseFormSet, modelformset_factory, formset_factory
from django.contrib.contenttypes.models import ContentType

from adin.core.forms import GenericCreateForm
from adin.core.widgets import SelectDateSpanishWidget
from accounting.models import Ledger_Template, Ledger, Ledger_Type, Charge
from accountables.models import Accountable, Accountable_Concept
from people.models import Person

class Ledger_TemplateCreateModelForm(GenericCreateForm):

    accountable_class = ModelChoiceField(
        queryset=ContentType.objects.filter(model__in=['lease_realty']),
        label='Clase Contabilizable'
    )

    class Meta:
        model = Ledger_Template
        fields = ['code', 'transaction_type', 'ledger_type', 'accountable_class']

    def save(self, creator_user, *args, **kwargs):
        base_args = {}
        base_args['code'] = self.cleaned_data.get('code')
        base_args['accountable_class'] = self.cleaned_data.get('accountable_class')
        base_args['ledger_type'] = self.cleaned_data.get('ledger_type')
        base_args['transaction_type'] = self.cleaned_data.get('transaction_type')
        base_args['concept_dependant'] = self.cleaned_data.get('concept_dependant')
        base_args['state_change_user'] = creator_user
        ledger_template = Ledger_Template(**base_args)
        ledger_template.save()
        return ledger_template

class Ledger_TemplateDetailModelForm(ModelForm):

    class Meta:
        model = Ledger_Template
        fields = ['code', 'transaction_type', 'ledger_type', 'accountable_class']

class Ledger_TemplateDeleteModelForm(ModelForm):

    class Meta:
        model = Ledger_Template
        fields = ['code', 'transaction_type', 'ledger_type', 'accountable_class']

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

    def clean(self):
        lt = self.cleaned_data.get('ledger_template')
        acc = self.cleaned_data.get('accountable')
        if not Accountable_Concept.pending.ledger(acc, lt).exists():
            self.add_error('accountable', 'Contabilizable no tiene conceptos pendientes para formato.')
        return super().clean()

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

    def concept_dependant(self):
        ledger_template = self.cleaned_data.get('ledger_template')
        return ledger_template.concept_dependant

class Ledger_TemplateConceptDataForm(Form):

    ledger_template = ModelChoiceField(
        queryset=Ledger_Template.objects.exclude(state=0),
        label='Formato Registro'
    )
    accountable = ModelChoiceField(
        queryset=Accountable.objects.exclude(state=0),
        label='Contabilizable'
    )
    date = DateField(
        widget=SelectDateSpanishWidget,
        label='Fecha Cargo'
    )
    value = IntegerField(
        label='Valor'
    )

    def __init__(self, *args, **kwargs):
        obj=kwargs['initial']['ledger_template']
        field_choices = {
            'accountable': obj.accountable_class.model_class().__bases__[0].objects.filter(code__in=obj.accountable_class.model_class().active.values_list('code', flat=True))
        }
        super(Ledger_TemplateConceptDataForm, self).__init__(*args, **kwargs)
        self.fields['accountable'].queryset = field_choices['accountable']

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date > datetime.date.today():
            self.add_error('date', "Fecha no puede ser posterior a hoy.")
        return date

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value <= 0:
            self.add_error('value', "Valor debe ser mayor que cero.")
        return value

    def clean(self):
        ledger_template = self.cleaned_data.get('ledger_template')
        accountable = self.cleaned_data.get('accountable')
        date = self.cleaned_data.get('date')
        value = self.cleaned_data.get('value')
        if Accountable_Concept.objects.exclude(state=0).filter(
            accountable=accountable,
            transaction_type=ledger_template.transaction_type,
            date=date,
            value=value
        ).exists():
            raise ValidationError(f'Concepto para estos datos ya existe.')
        return super().clean()

    def save(self):
        ledger_template = self.cleaned_data.get('ledger_template')
        accountable = self.cleaned_data.get('accountable')
        date = self.cleaned_data.get('date')
        value = self.cleaned_data.get('value')
        led=Ledger(
            type=ledger_template.ledger_type,
            holder=accountable.subclass_obj().primary_lessor(),
            third_party=accountable.subclass_obj().lessee(),
            date=date,
            state_change_user=self.creator
        )
        led.save()
        acc_con=Accountable_Concept(
            accountable=accountable,
            transaction_type=ledger_template.transaction_type,
            date=date,
            value=value,
            state_change_user=self.creator
        )
        acc_con.save()
        for cha_tem in ledger_template.charges_templates.all():
            Charge(
                ledger=led,
                account=cha_tem.account,
                value=cha_tem.factor.factored_value(accountable, acc_con.date, acc_con.value, cha_tem.nature),
                concept=acc_con,
            state_change_user=self.creator
            ).save()
        acc_con.save()
        return led 

class Ledger_TemplateSelectConceptForm(Form):

    ledger_template = ModelChoiceField(
        queryset=Ledger_Template.objects.exclude(state=0),
        label='Formato Registro'
    )
    accountable_concept = ModelChoiceField(
        queryset=Accountable_Concept.objects.exclude(state=0),
        label='Concepto Transaccion'
    )
    ledger_type = ModelChoiceField(
        queryset=Ledger_Type.objects.exclude(state=0),
        label='Tipo Registro'
    )
    accountable = ModelChoiceField(
        queryset=Accountable.objects.exclude(state=0),
        label='Contabilizable'
    )
    holder = ModelChoiceField(
        queryset=Person.objects.exclude(state=0),
        label='Titular'
    )
    third_party = ModelChoiceField(
        queryset=Person.objects.exclude(state=0),
        label='Tercero'
    )
    concept_date = DateField(
        label='Fecha Concepto'
    )
    concept_value = IntegerField(
        label='Valor Base'
    )

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

    def save(self, user):
        led_tem = self.cleaned_data.get('ledger_template')
        acc_con = self.cleaned_data.get('accountable_concept')
        return led_tem.create_ledger(acc_con, acc_con.date, user)

class Ledger_TemplateBulkPendingCreateBaseFormSet(BaseFormSet):

    def save(self, user):
        for form in self.forms:
            form.save(user)

Ledger_TemplateBulkPendingCreateFormSet =  formset_factory(form=Ledger_TemplateSelectConceptForm, formset=Ledger_TemplateBulkPendingCreateBaseFormSet, extra=0)

Ledger_TemplateListModelFormSet = modelformset_factory(Ledger_Template, fields=('code', 'accountable_class'), extra=0)

Ledger_TemplateAvailableModelFormset = modelformset_factory(Ledger_Template, fields=('code', ), extra=0)
