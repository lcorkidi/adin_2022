from django.forms import modelformset_factory, SelectDateWidget

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm
from properties.models.estate import Estate_Appraisal

class Estate_AppraisalCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Estate_Appraisal
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

class Estate_AppraisalUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Estate_Appraisal
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

Estate_AppraisalModelFormSet = modelformset_factory(Estate_Appraisal, fields=('state', 'type', 'date', 'value'), extra=0)