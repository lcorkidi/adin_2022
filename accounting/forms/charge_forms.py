from django.forms import Form, IntegerField, ModelChoiceField, IntegerField, formset_factory, modelformset_factory

from accounting.models import Charge, Charge_Concept, Account
 
class ChaCreateForm(Form):

    account = ModelChoiceField(
        queryset=Account.objects.all(),
        label='Cuenta'
    )
    concept = ModelChoiceField(
        queryset=Charge_Concept.objects.all(),
        label='Concepto'
    )
    debit = IntegerField(
        label='Débito'
    )
    credit = IntegerField(
        label='Crédito'
    )

ChargeCreateFormset = formset_factory(ChaCreateForm, extra=2)

ChargeModelFormSet = modelformset_factory(Charge, fields=('state', 'account', 'value', 'concept'), extra=0)
