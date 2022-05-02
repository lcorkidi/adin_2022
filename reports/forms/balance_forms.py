from attr import attr
from django.forms import Form, CharField, IntegerField, BooleanField, NumberInput, formset_factory

class AccountBalanceForm(Form):

    account = IntegerField(
        label='Cuenta'
    )
    name = CharField(
        label='Nombre'
    )
    previous_balance = IntegerField(
        widget=NumberInput(attrs={'currency':True, 'show_zero': True}),
        label='Saldo Anterior'
    )
    debit = IntegerField(
        widget=NumberInput(attrs={'currency':True, 'show_zero': True, 'detail': True}),
        label='Débito'
    )
    credit = IntegerField(
        widget=NumberInput(attrs={'currency':True, 'show_zero': True, 'detail': True}),
        label='Crédito'
    )
    closing_balance = IntegerField(
        widget=NumberInput(attrs={'currency':True, 'show_zero': True, 'detail': True}),
        label='Saldo Posterior'
    )
    priority = IntegerField(
        label='priority'
    )
    chargeable = BooleanField(
        label='chargeable'
    )

AccountBalanceFormSet = formset_factory(AccountBalanceForm, extra=0)
