from django import forms

from references.models import Address
from scripts.utils import address2code

class AddressDetailModelForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ['code']

class AddressCreateModelForm(forms.ModelForm):

    class Meta:
        model = Address
        exclude = ('code',)

    def save(self, *args, **kwargs):
        base_args = {k: self.cleaned_data[k] for k in self.fields}
        base_args['state_change_user'] = self.creator
        add = Address(**base_args)
        add.code = address2code(add)
        add.save()
        return add

AddressListModelFormSet = forms.modelformset_factory(Address, fields=('code',), extra=0)
