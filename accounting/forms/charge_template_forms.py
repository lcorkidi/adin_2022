from django.forms import Form, BaseFormSet, TypedChoiceField, ModelChoiceField, ValidationError, formset_factory, modelformset_factory

from accounting.models import Charge_Template, Account
from references.models import Charge_Factor
 
class Charge_TemplateCreateForm(Form):

    NATURE_CHOICE = [
        ('', '----'),
        (-1, 'Credito'),
        (1, 'Debito'),
    ]

    account = ModelChoiceField(
        queryset=Account.chargeables.all(),
        required=False,
        label='Cuenta'
    )
    factor = ModelChoiceField(
        queryset=Charge_Factor.objects.all(),
        label='Tasa'
    )
    nature = TypedChoiceField(
        choices=NATURE_CHOICE,
        empty_value='',
        initial='',
        label='Naturaleza'
    )

    def clean(self):
        cleaned_data = super().clean()
        account = cleaned_data.get('account')
        factor = cleaned_data.get('factor')
        nature = cleaned_data.get('nature')
        if account or factor or nature != '':
            if not account:
                msg = f'Falta seleccionar cuenta.'
                self.add_error('account', msg)
            if not factor:
                msg = f'Falta seleccionar factor.'
                self.add_error('factor', msg)
            if nature == '':
                msg = f'Falta seleccionar naturaleza.'
                self.add_error('nature', msg)
        return cleaned_data

    def is_empty(self):
        account = self.cleaned_data.get('account')
        factor = self.cleaned_data.get('factor')
        nature =self. cleaned_data.get('nature')
        if account or factor or nature not in [None, '']:
            return False
        return True

    def save(self, ledger_template, creator_user, *args, **kwargs):
        base_args = {}
        print((ledger_template, creator_user))
        base_args['ledger_template'] = ledger_template
        base_args['account'] = self.cleaned_data.get('account')
        base_args['factor'] = self.cleaned_data.get('factor')
        base_args['nature'] = self.cleaned_data.get('nature')
        base_args['state_change_user'] = creator_user
        Charge_Template(**base_args).save()

class Charge_TemplateBareFormSet(BaseFormSet):
    
    def clean(self):
        if any(self.errors):
            return
        if all(f.is_empty() for f in self.forms):
            raise ValidationError('No hay formatos movimientos.')
        return super().clean()

    def save(self, ledger_template, creator_user, *args, **kwargs):
        for form in self.forms:
            if not all(form[f].value() in [None, ''] for f in form.fields):
                form.save(ledger_template, creator_user)

Charge_TemplateCreateFormset = formset_factory(Charge_TemplateCreateForm, formset=Charge_TemplateBareFormSet, extra=20)

Charge_TemplateModelFormSet = modelformset_factory(Charge_Template, fields=('account', 'factor', 'nature'), extra=0)
