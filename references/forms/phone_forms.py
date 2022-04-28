from django.forms import ModelForm, ValidationError, modelformset_factory

from adin.core.forms import GenericCreateForm, GenericDeleteForm, GenericActivateForm
from references.models import Phone
from references.utils import phone2code

class PhoneCreateModelForm(GenericCreateForm):

    class Meta:
        model = Phone
        exclude = ('state', 'code',)

    def clean(self):
        base_args = {}
        for field in self.fields:
            if field:
                base_args[field] = self.cleaned_data[field]
        obj = Phone(**base_args)
        code = phone2code(obj)
        if Phone.objects.filter(pk=code).exists():
            obj = Phone.objects.get(pk=code)
            if obj.state == 0:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con estos datos ya existe y está inactiva.")
            else:
                raise ValidationError(f"{self._meta.model._meta.verbose_name} con estos datos ya existe.")
        return super().clean()

class PhoneDetailModelForm(ModelForm):

    class Meta:
        model = Phone
        fields = ['state', 'code']

class PhoneDeleteModelForm(GenericDeleteForm):

    class Meta:
        model = Phone
        fields = ['code']

class PhoneActivateModelForm(GenericActivateForm):

    class Meta:
        model = Phone
        fields = ['code']

PhoneListModelFormSet = modelformset_factory(Phone, fields=('state', 'code',), extra=0)
