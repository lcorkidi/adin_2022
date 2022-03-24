from django.forms import modelformset_factory, SelectDateWidget

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm
from accountables.models import Date_Value

class Date_ValueCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Date_Value
        exclude = ('state',)
        widgets = {
            'date': SelectDateWidget(
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

class Date_ValueUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Date_Value
        exclude = ('state',)
        widgets = {
            'date': SelectDateWidget(
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

Date_ValueModelFormSet = modelformset_factory(Date_Value, fields=('state', 'date', 'value'), extra=0)