from attr import attr
from django.forms import Form, CharField, IntegerField, TextInput, NumberInput, formset_factory

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
        widget=NumberInput(attrs={'currency':True, 'show_zero': True}),
        label='Debito'
    )
    credit = IntegerField(
        widget=NumberInput(attrs={'currency':True, 'show_zero': True}),
        label='Debito'
    )
    closing_balance = IntegerField(
        widget=NumberInput(attrs={'currency':True, 'show_zero': True}),
        label='Saldo Posterior'
    )

AccountBalanceFormSet = formset_factory(AccountBalanceForm, extra=0)
