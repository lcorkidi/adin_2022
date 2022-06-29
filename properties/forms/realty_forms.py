from django.forms import ModelForm, ValidationError, modelformset_factory

from adin.core.forms import GenericCreateForm, GenericUpdateForm, GenericDeleteForm, GenericActivateForm
from properties.models import Realty

class RealtyCreateForm(GenericCreateForm):

    pk_name = 'code'

    class Meta:
        model = Realty
        fields = [ 'address', 'type', 'use', 'total_area' ]

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if address.state == 0:
            self.add_error('address', f'Dirección seleccionada inactiva.')
        if self._meta.model.objects.filter(address=address).exists():
            obj = self._meta.model.objects.get(address=address)
            if obj.state == 0:
                raise ValidationError(f"El inmueble {Realty.objects.get(address=address)} ya tiene esta dirección y está inactivo.")
            else:
                raise ValidationError(f"El inmueble {Realty.objects.get(address=address)} ya tiene esta dirección.")
        return address

class RealtyDetailForm(ModelForm):

    class Meta:
        model = Realty
        fields = ['state',  'code', 'address', 'type', 'use', 'total_area' ]

class RealtyUpdateForm(GenericUpdateForm):

    class Meta:
        model = Realty
        fields = [ 'code', 'address', 'type', 'use', 'total_area' ]

class RealtyDeleteForm(GenericDeleteForm):

    class Meta:
        model = Realty
        fields = [ 'code', 'address', 'type', 'use', 'total_area' ]

class RealtyActivateForm(GenericActivateForm):

    class Meta:
        model = Realty
        fields = [ 'code', 'address', 'type', 'use', 'total_area' ]

    def clean_address(self):
        address = self.cleaned_data['address']
        if address.state == 0:
                self.add_error(None, f'Dirección del inmueble inactiva.')
        return address

RealtyListModelFormSet = modelformset_factory(Realty, fields=('state', 'code', 'use', 'total_area'), extra=0)