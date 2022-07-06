import datetime
from django.forms import ModelForm, SelectDateWidget, modelformset_factory

from adin.core.forms import GenericCreateForm, GenericDeleteForm, GenericActivateForm
from references.models import Calendar_Date

class Calendar_DateCreateForm(GenericCreateForm):

    pk_name = 'name'

    class Meta:
        model = Calendar_Date
        fields = ['name', 'date']
        widgets = {
            'date': SelectDateWidget(
                years=range(1970, datetime.date.today().year + 1),
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

    def clean_name(self):
        return self.clean_pk()

class Calendar_DateDetailModelForm(ModelForm):

    class Meta:
        model = Calendar_Date
        fields = ['state', 'name', 'date']

class Calendar_DateDeleteModelForm(GenericDeleteForm):

    class Meta:
        model = Calendar_Date
        fields = ['name', 'date']

class Calendar_DateActivateModelForm(GenericActivateForm):

    class Meta:
        model = Calendar_Date
        fields = ['name', 'date']

Calendar_DateListModelFormSet = modelformset_factory(Calendar_Date, fields=('state', 'name', 'date'), extra=0)
