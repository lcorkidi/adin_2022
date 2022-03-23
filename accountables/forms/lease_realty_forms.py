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
        label='Propiedades Secundarias'
    )
    doc_date = DateField(
        widget=SelectDateWidget(),
        label = 'Fecha Contrato:'
    )
    fee = IntegerField(
        min_value=0,
        label='Mensualidad:'
    )

    def clean(self):
        cleaned_data = super().clean()
        realty = cleaned_data.get('realty')


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