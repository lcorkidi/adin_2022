from django.forms import BaseModelFormSet, modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericDeleteRelatedForm, GenericActivateRelatedForm
from accountables.models import Lease_Realty_Realty

class Lease_Realty_RealtyCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Lease_Realty_Realty
        exclude = ('state', 'primary')

    def clean_realty(self):
        realty = self.cleaned_data['realty']
        if realty.state == 0:
            self.add_error('realty', f'Inmueble seleccionado inactivo.')
        return realty

    def save(self, *args, **kwargs):
        base_args = {k: self.cleaned_data[k] for k in self.fields}
        base_args['primary'] = False
        base_args['state_change_user'] = self.creator
        obj = self._meta.model(**base_args)
        obj.save()
        return obj

class Lease_Realty_RealtyDeleteForm(GenericDeleteRelatedForm):

    class Meta:
        model = Lease_Realty_Realty
        exclude = ('state',)

    def clean(self):
        primary = self.instance.primary
        if primary:
            self.add_error(None, 'No se puede borrar inmueble primario.')
        return super().clean()

class Lease_Realty_RealtyActivateForm(GenericActivateRelatedForm):

    related_fields = ['lease', 'realty']

    class Meta:
        model = Lease_Realty_Realty
        exclude = ('state',)

class Lease_Realty_RealtyRelatedUpdateBaseModelFormSet(BaseModelFormSet):

    def __init__(self, rel_pk, *args, **kwargs):
        super(Lease_Realty_RealtyRelatedUpdateBaseModelFormSet, self).__init__(*args, **kwargs)

Lease_Realty_RealtyModelFormSet = modelformset_factory(Lease_Realty_Realty, formset=Lease_Realty_RealtyRelatedUpdateBaseModelFormSet, fields=('state',  'realty', 'primary'), extra=0)