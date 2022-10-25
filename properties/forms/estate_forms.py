from django.forms import ModelForm, ValidationError, modelformset_factory

from adin.core.forms import GenericCreateForm, GenericUpdateForm, GenericDeleteForm, GenericActivateForm
from properties.models import Estate

class EstateCreateForm(GenericCreateForm):

    pk_name = 'national_number'

    class Meta:
        model = Estate
        fields = [ 'national_number', 'address', 'total_area']

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if address.state == 0:
            self.add_error('address', f'Dirección seleccionada inactiva.')
        if self._meta.model.objects.filter(address=address).exists():
            obj = self._meta.model.objects.get(address=address)
            if obj.state == 0:
                raise ValidationError(f"El predio {Estate.objects.get(address=address)} ya tiene esta dirección y está inactivo.")
            else:
                raise ValidationError(f"El predio {Estate.objects.get(address=address)} ya tiene esta dirección.")
        return address

    def clean_national_number(self):
        return self.clean_pk()

class EstateDetailForm(ModelForm):

    class Meta:
        model = Estate
        fields = ['state',  'national_number', 'address', 'total_area']

class EstateUpdateForm(GenericUpdateForm):

    class Meta:
        model = Estate
        fields = ['state', 'national_number', 'address', 'total_area']

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if self.has_changed():
            if address.state == 0:
                self.add_error('address', f'Dirección seleccionada inactiva.')
            if self._meta.model.objects.filter(address=address).exists():
                obj = self._meta.model.objects.get(address=address)
                if obj.state == 0:
                    raise ValidationError(f"El predio {Estate.objects.get(address=address)} ya tiene esta dirección y está inactivo.")
                else:
                    raise ValidationError(f"El predio {Estate.objects.get(address=address)} ya tiene esta dirección.")
        return address

class EstateDeleteForm(GenericDeleteForm):

    exclude_fields = ['estate_appraisal']

    class Meta:
        model = Estate
        fields = ['state', 'national_number', 'address', 'total_area']

class EstateActivateForm(GenericActivateForm):

    class Meta:
        model = Estate
        fields = [ 'national_number', 'address', 'total_area']

    def clean_address(self):
        address = self.cleaned_data['address']
        if address.state == 0:
                self.add_error(None, f'Dirección del predio inactiva.')
        return address

EstateListModelFormSet = modelformset_factory(Estate, fields=('state', 'national_number', 'address', 'total_area'), extra=0)