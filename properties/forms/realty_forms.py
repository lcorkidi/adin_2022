from django.forms import ModelForm, ValidationError, modelformset_factory

from adin.core.forms import GenericCreateForm, GenericUpdateForm, GenericDeleteForm
from properties.models import Realty

class RealtyCreateForm(GenericCreateForm):

    pk_name = 'code'

    class Meta:
        model = Realty
        fields = [ 'address', 'type', 'use', 'total_area' ]

    def clean_address(self):
        data = self.cleaned_data.get('address')
        if self._meta.model.objects.filter(address=data).exists():
            obj = self._meta.model.objects.get(address=data)
            if obj.state == 0:
                raise ValidationError(f"El inmueble {Realty.objects.get(address=data)} ya tiene esta dirección y está inactivo.")
            else:
                raise ValidationError(f"El inmueble {Realty.objects.get(address=data)} ya tiene esta dirección.")
        return data

class RealtyDetailForm(ModelForm):

    class Meta:
        model = Realty
        fields = [ 'code', 'address', 'type', 'use', 'total_area' ]

class RealtyUpdateForm(GenericUpdateForm):

    class Meta:
        model = Realty
        fields = [ 'code', 'address', 'type', 'use', 'total_area' ]

class RealtyDeleteForm(GenericDeleteForm):

    class Meta:
        model = Realty
        fields = [ 'code', 'address', 'type', 'use', 'total_area' ]

RealtyListModelFormSet = modelformset_factory(Realty, fields=('code', 'use', 'total_area'), extra=0)