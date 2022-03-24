from django.forms import ModelForm, ValidationError, modelformset_factory

from adin.core.forms import GenericCreateForm, GenericUpdateForm, GenericDeleteForm
from properties.models import Estate

class EstateCreateForm(GenericCreateForm):

    pk_name = 'national_number'

    class Meta:
        model = Estate
        fields = [ 'national_number', 'address', 'total_area']

    def clean_address(self):
        data = self.cleaned_data.get('address')
        if self._meta.model.objects.filter(address=data).exists():
            obj = self._meta.model.objects.get(address=data)
            if obj.state == 0:
                raise ValidationError(f"El predio {Estate.objects.get(address=data)} ya tiene esta dirección y está inactivo.")
            else:
                raise ValidationError(f"El predio {Estate.objects.get(address=data)} ya tiene esta dirección.")
        return data

    def clean_national_number(self):
        return self.clean_pk()

class EstateDetailForm(ModelForm):

    class Meta:
        model = Estate
        fields = ['state',  'national_number', 'address', 'total_area']

class EstateUpdateForm(GenericUpdateForm):

    class Meta:
        model = Estate
        fields = [ 'national_number', 'address', 'total_area']

    def clean_address(self):
        data = self.cleaned_data.get('address')
        if 'address' in self.changed_data:
            if self._meta.model.objects.filter(address=data).exists():
                obj = self._meta.model.objects.get(address=data)
                if obj.state == 0:
                    raise ValidationError(f"El predio {Estate.objects.get(address=data)} ya tiene esta dirección y está inactivo.")
                else:
                    raise ValidationError(f"El predio {Estate.objects.get(address=data)} ya tiene esta dirección.")
        return data

class EstateDeleteForm(GenericDeleteForm):

    class Meta:
        model = Estate
        fields = [ 'national_number', 'address', 'total_area']

EstateListModelFormSet = modelformset_factory(Estate, fields=('state', 'national_number', 'address', 'total_area'), extra=0)