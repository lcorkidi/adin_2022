from django.forms import Form, CharField, IntegerField, NumberInput, DateField, DateInput, formset_factory

class ChargeReportForm(Form):

    ledger = CharField(
        label='Registro'
    )
    date = DateField(
        widget=DateInput(attrs={'date':True}),
        label='Fecha'
    )
    third_party = CharField(
        label='Tercero'
    )
    accountable = CharField(
        label='Documento Concepto'
    )
    concept = CharField(
        label='Tipo Concepto'
    )
    concept__date = DateField(
        widget=DateInput(attrs={'date':True}),
        label='Fecha Concepto'
    )
    account = CharField(
        label='Cuenta'
    )
    debit = IntegerField(
        widget=NumberInput(attrs={'currency':True, 'show_zero': False}),
        label='Débito'
    )
    credit = IntegerField(
        widget=NumberInput(attrs={'currency':True, 'show_zero': False}),
        label='Crédito'
    )

ChargeReportFormSet = formset_factory(ChargeReportForm, extra=0)
