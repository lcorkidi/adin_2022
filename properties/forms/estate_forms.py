from django.forms import ModelForm, ValidationError, modelformset_factory

from adin.core.forms import GenericCreateForm, GenericUpdateForm, GenericDeleteForm
from properties.models import Estate

class EstateCreateForm(GenericCreateForm):

    pk_name = 'address'

    class Meta:
        model = Estate
        fields = [ 'national_number_1', 'national_number_2', 'national_number_3', 'address', 'total_area']

    def clean_address(self):
        data = self.cleaned_data.get(self.pk_name)
        if self._meta.model.objects.filter(pk=data.pk).exists():
            obj = self._meta.model.objects.get(pk=data.pk)
            if obj.state == 0:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con {self._meta.model._meta.get_field(self.pk_name).verbose_name} ya existe y está inactiva.")
            else:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con {self._meta.model._meta.get_field(self.pk_name).verbose_name} ya existe.")
        return data

class EstateDetailForm(ModelForm):

    class Meta:
        model = Estate
        fields = [ 'national_number_1', 'national_number_2', 'national_number_3', 'code', 'address', 'total_area']

class EstateUpdateForm(GenericUpdateForm):

    class Meta:
        model = Estate
        fields = [ 'national_number_1', 'national_number_2', 'national_number_3', 'code', 'address', 'total_area']

    def clean_address(self):
        data = self.cleaned_data.get('address')
        if self._meta.model.objects.filter(address=data.pk).exists():
            obj = self._meta.model.objects.get(address=data.pk)
            if obj.state == 0:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con {self._meta.model._meta.get_field('address').verbose_name} ya existe y está inactiva.")
            else:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con {self._meta.model._meta.get_field('address').verbose_name} ya existe.")
        return data

class EstateDeleteForm(GenericDeleteForm):

    class Meta:
        model = Estate
        fields = [ 'national_number_1', 'national_number_2', 'national_number_3', 'code', 'address', 'total_area']

EstateListModelFormSet = modelformset_factory(Estate, fields=('code', 'total_area'), extra=0)