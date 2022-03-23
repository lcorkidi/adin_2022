from django.forms import ModelForm, Form, ModelChoiceField, ModelMultipleChoiceField, DateField, SelectDateWidget, IntegerField, modelformset_factory

from adin.core.forms import GenericUpdateForm, GenericDeleteForm
from accountables.models import Lease_Realty
from properties.models.realty import Realty

class Lease_RealtyCreateForm(Form):

    realty = ModelChoiceField(
        queryset=Realty.objects.all(),
        label='Propiedad Principal:'
    )
    realties = ModelMultipleChoiceField(
        queryset=Realty.objects.all(),
        required=False,
        label='Propiedades Secundarias'
    )
    doc_date = DateField(
        widget=SelectDateWidget(
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
        ),
        label = 'Fecha Contrato:'
    )
    fee = IntegerField(
        min_value=0,
        label='Mensualidad:'
    )

    def clean(self):
        cleaned_data = super().clean()
        realty = cleaned_data.get('realty')

        print(realty.is_vacant())

    def save(self):
        pass

class Lease_RealtyDetailForm(ModelForm):

    class Meta:
        model = Lease_Realty
        fields = [ 'code', 'doc_date', 'start_date', 'end_date']

class Lease_RealtyUpdateForm(GenericUpdateForm):

    class Meta:
        model = Lease_Realty
        fields = [ 'code', 'doc_date', 'start_date', 'end_date']

class Lease_RealtyDeleteForm(GenericDeleteForm):

    class Meta:
        model = Lease_Realty
        fields = [ 'code', 'doc_date', 'start_date', 'end_date']

Lease_RealtyListModelFormSet = modelformset_factory(Lease_Realty, fields=('code',), extra=0)