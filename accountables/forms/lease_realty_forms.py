from django.forms import ModelForm, Form, ModelChoiceField, ModelMultipleChoiceField, DateField, IntegerField, modelformset_factory
from django.contrib.contenttypes.models import ContentType

from adin.core.forms import GenericUpdateForm, GenericDeleteForm, GenericActivateForm
from adin.core.widgets import SelectDateSpanishWidget
from accountables.models import Lease_Realty, Lease_Realty_Realty, Date_Value
from accountables.utils.views_data import lease_realty_code
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
        widget=SelectDateSpanishWidget(),
        label = 'Fecha Contrato:'
    )
    fee = IntegerField(
        min_value=0,
        label='Mensualidad:'
    )

    def clean(self):
        cleaned_data = super().clean()
        realty = cleaned_data.get('realty')
        ralties = cleaned_data.get('realties')
        if not realty.is_vacant():
            msg = 'Propiedad está ocupada.'
            self.add_error('realty', msg)
        for _realty in ralties:
            if realty == _realty:
                msg = f'Propiedad {_realty} ya escogida como principal.'
                self.add_error('realties', msg)
            if not _realty.is_vacant():
                msg = f'Propiedad {_realty} está ocupada.'
                self.add_error('realties', msg)
        return cleaned_data

    def save(self):
        realty = self.cleaned_data.get('realty')
        realties = self.cleaned_data.get('realties')
        doc_date = self.cleaned_data.get('doc_date')
        value = self.cleaned_data.get('fee')
        subclass = ContentType.objects.get(model='lease_realty')
        lea_rea = Lease_Realty(code=lease_realty_code(realty, doc_date), subclass=subclass, doc_date=doc_date, state_change_user=self.creator)
        lea_rea.save()
        lea_rea_rea = Lease_Realty_Realty(lease=lea_rea, realty=realty, primary=True, state_change_user=self.creator)
        lea_rea_rea.save()
        for _realty in realties:
            _lea_rea_rea = Lease_Realty_Realty(lease=lea_rea, realty=_realty, primary=False, state_change_user=self.creator)
            _lea_rea_rea.save()
        dat_val = Date_Value(accountable=lea_rea, date=doc_date, value=value, state_change_user=self.creator)
        dat_val.save()

class Lease_RealtyDetailForm(ModelForm):

    class Meta:
        model = Lease_Realty
        fields = ['state',  'code', 'doc_date', 'start_date', 'end_date']

class Lease_RealtyUpdateForm(GenericUpdateForm):

    class Meta:
        model = Lease_Realty
        fields = [ 'code', 'doc_date', 'start_date', 'end_date']
        widgets = {
            'doc_date': SelectDateSpanishWidget(), 
            'start_date': SelectDateSpanishWidget(), 
            'end_date': SelectDateSpanishWidget()
        }

    def clean(self):
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        if end_date and not start_date:
            self.add_error('end_date', 'No puede haber desocupación sin ocupación.')
        if start_date and end_date and end_date <= start_date:
            self.add_error('end_date', 'Desocupación no puede ser anterior a ocupación.')
        return super().clean()

class Lease_RealtyAccoutingForm(ModelForm):

    class Meta:
        model = Lease_Realty
        fields = ['state',  'code']

class Lease_RealtyDeleteForm(GenericDeleteForm):

    exclude_fields = ['dates_values']

    class Meta:
        model = Lease_Realty
        fields = [ 'code', 'doc_date', 'start_date', 'end_date']

class Lease_RealtyActivateForm(GenericActivateForm):

    class Meta:
        model = Lease_Realty
        fields = [ 'code', 'doc_date', 'start_date', 'end_date']

Lease_RealtyListModelFormSet = modelformset_factory(Lease_Realty, fields=('state', 'code',), extra=0)