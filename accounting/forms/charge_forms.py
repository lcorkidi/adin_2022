from django.forms import Form, BaseFormSet, CharField, DateField, IntegerField, ModelChoiceField, IntegerField, ValidationError, formset_factory, modelformset_factory

from accounting.models import Charge, Charge_Concept, Account

class ChargeReportForm(Form):

    ledger = CharField(
        label='Código Registro'
    )
    ledger__date = DateField(
        label='Fecha Registro'
    )
    ledger__third_party = CharField(
        label='Tercero Registro'
    )
    concept__accountable = CharField(
        label='Documento Concepto'
    )
    concept__transaction_type = CharField(
        label='Tipo Concepto'
    )
    concept__date = DateField(
        label='Fecha Concepto'
    )
    account = CharField(
        label='Cuenta'
    )
    value = CharField(
        label='Valor'
    )

ChargeReportFormSet = formset_factory(ChargeReportForm, extra=0)
 
class ChargeCreateForm(Form):

    account = ModelChoiceField(
        queryset=Account.chargeables.all(),
        required=False,
        label='Cuenta'
    )
    concept = ModelChoiceField(
        queryset=Charge_Concept.objects.all(),
        required=False,
        label='Concepto'
    )
    debit = IntegerField(
        required=False,
        label='Débito'
    )
    credit = IntegerField(
        required=False,
        label='Crédito'
    )

    def clean(self):
        cleaned_data = super().clean()
        account = cleaned_data.get('account')
        concept = cleaned_data.get('concept')
        debit = cleaned_data.get('debit')
        credit = cleaned_data.get('credit')
        if account or concept or (debit and debit != 0) or (credit and credit != 0):
            if not account:
                msg = f'Falta seleccionar cuenta.'
                self.add_error('account', msg)
            if not concept:
                msg = f'Falta seleccionar concepto.'
                self.add_error('concept', msg)
            if not debit and not credit:
                msg = f'Falta un valor.'
                self.add_error('debit', msg)
                self.add_error('credit', msg)
        if debit and credit and debit > 0 and credit > 0:
            msg = f'Los campos credito y debito no pueden ambos tener un valor.'
            self.add_error('debit', msg)
            self.add_error('credit', msg)
        return cleaned_data

    def clean_debit(self):
        data = self.cleaned_data.get('debit')
        if data and data < 0:
            msg = f'Valor no puede ser menor que cero.'
            self.add_error('debit', msg)
        return data

    def clean_credit(self):
        data = self.cleaned_data.get('credit')
        if data and data < 0:
            msg = f'Valor no puede ser menor que cero.'
            self.add_error('credit', msg)
        return data

    def is_empty(self):
        account = self.cleaned_data.get('account')
        concept = self.cleaned_data.get('concept')
        debit =self. cleaned_data.get('debit')
        credit = self.cleaned_data.get('credit')
        if account or concept or (debit and debit != 0) or (credit and credit != 0):
            return False
        return True

    def save(self, *args, **kwargs):
        base_args = {}
        base_args['ledger'] = args[0]
        base_args['account'] = self.cleaned_data.get('account')
        base_args['concept'] = self.cleaned_data.get('concept')
        debit = self.cleaned_data.get('debit')
        if debit and debit > 0:
            base_args['value'] = debit
        else:
            base_args['value'] = -self.cleaned_data.get('credit')
        base_args['state_change_user'] = self.creator
        obj = Charge(**base_args)
        obj.save()
        return obj

class ChargeBareFormSet(BaseFormSet):
    
    def clean(self):
        if any(self.errors):
            return
        if all(f.is_empty() for f in self.forms):
            raise ValidationError('No hay movimientos.')
        debit_sum = 0
        credit_sum = 0
        for form in self.forms:
            debit = form.cleaned_data.get('debit')
            if debit:
                debit_sum += debit
            credit = form.cleaned_data.get('credit')
            if credit:
                credit_sum += credit
        if debit_sum != credit_sum:
            raise ValidationError('Valores debito y credito deben estar balanceados.')
        return super().clean()

    def save(self, *args, **kwargs):
        for form in self.forms:
            if not all(form[f].value() in [None, ''] for f in form.fields):
                form.creator = self.creator
                form.save(args[0])

ChargeCreateFormset = formset_factory(ChargeCreateForm, formset=ChargeBareFormSet, extra=20)

ChargeModelFormSet = modelformset_factory(Charge, fields=('state', 'account', 'value', 'concept'), extra=0)
