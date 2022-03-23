from django.forms import ModelForm, ValidationError, modelformset_factory

from adin.core.forms import GenericCreateForm, GenericDeleteForm
from references.models import Address
from references.utils import address2code

class AddressCreateModelForm(GenericCreateForm):

    class Meta:
        model = Address
        exclude = ('code',)

    def clean(self):
        base_args = {}
        for field in self.fields:
            if field:
                base_args[field] = self.cleaned_data[field]
        obj = Address(**base_args)
        code = address2code(obj)
        if Address.objects.filter(pk=code).exists():
            obj = Address.objects.get(pk=code)
            if obj.state == 0:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con estos datos ya existe y está inactiva.")
            else:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con estos datos ya existe.")
        return super().clean()

class AddressDetailModelForm(ModelForm):

    class Meta:
        model = Address
        fields = ['code']

class AddressDeleteModelForm(GenericDeleteForm):

    class Meta:
        model = Address
        fields = ['code']

AddressListModelFormSet = modelformset_factory(Address, fields=('code',), extra=0)
