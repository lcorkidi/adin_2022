import datetime
from django.forms import ModelForm, SelectDateWidget, modelformset_factory

from adin.core.forms import GenericCreateForm, GenericDeleteForm
from accounting.models import Ledger

class LedgerCreateModelForm(GenericCreateForm):

    class Meta:
        model = Ledger
        fields = ['type', 'holder', 'third_party', 'date', 'description']
        widgets = {
            'date': SelectDateWidget(
                years=range(datetime.date.today().year - 1, datetime.date.today().year + 1),
                months= {
                    1: 'Enero',
                    2: 'Febrero',
                    3: 'Marzo',
                    4: 'Abril',
                    5: 'Mayo',
                    6: 'Junio',
                    7: 'Julio',
                    8: 'Agosto',
                    9: 'Septiembre',
                    10: 'Octubre',
                    11: 'Noviembre',
                    12: 'Diciembre'
                }
            )
        }

class LedgerDetailModelForm(ModelForm):

    class Meta:
        model = Ledger
        fields = ['state', 'code', 'holder', 'third_party', 'date', 'description']

class LedgerDeleteModelForm(GenericDeleteForm):

    class Meta:
        model = Ledger
        fields = ['code', 'holder', 'third_party', 'date', 'description']

LedgerListModelFormSet = modelformset_factory(Ledger, fields=('state', 'code', 'holder', 'third_party', 'date'), extra=0)
