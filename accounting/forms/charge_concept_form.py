import datetime
from django.forms import ModelForm, SelectDateWidget, ValidationError, modelformset_factory

from adin.core.forms import GenericCreateForm, GenericDeleteForm
from accounting.models import Charge_Concept
from accounting.utils import chacon2code

class Charge_ConceptCreateModelForm(GenericCreateForm):

    class Meta:
        model = Charge_Concept
        fields = ['accountable', 'transaction_type', 'date']
        widgets = {
            'date': SelectDateWidget(
                years= range(datetime.date.today().year - 10, datetime.date.today().year + 10),
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

    def clean(self):
        base_args = {}
        for field in self.fields:
            if field:
                base_args[field] = self.cleaned_data[field]
        obj = Charge_Concept(**base_args)
        code = chacon2code(obj)
        if Charge_Concept.objects.filter(pk=code).exists():
            obj = Charge_Concept.objects.get(pk=code)
            if obj.state == 0:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con estos datos ya existe y está inactiva.")
            else:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con estos datos ya existe.")
        return super().clean()

class Charge_ConceptDetailModelForm(ModelForm):

    class Meta:
        model = Charge_Concept
        fields = ['state', 'code', 'accountable', 'transaction_type', 'date']

class Charge_ConceptDeleteModelForm(GenericDeleteForm):

    class Meta:
        model = Charge_Concept
        fields = ['code', 'accountable', 'transaction_type', 'date']

Charge_ConceptListModelFormSet = modelformset_factory(Charge_Concept, fields=('state', 'code'), extra=0)
