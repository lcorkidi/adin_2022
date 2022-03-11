from django import forms

from references.models import Address

class AddressCreateModelForm(forms.ModelForm):

    class Meta:
        model = Address
        exclude = ('code',)

    def save(self, *args, **kwargs):
        base_args = {k: self.cleaned_data[k] for k in self.fields}
        base_args['state_change_user'] = self.creator
        add = Address(**base_args)
        add.save()
        return add

class AddressDetailModelForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ['code']

class AddressDeleteModelForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ['code']

    def clean(self):
        objs = []
        for obj in self.instance._meta._get_fields(forward=False, reverse=True, include_hidden=True):
            if (not obj.hidden or obj.field.many_to_many) and obj.related_name: 
                for obj in eval(f'self.instance.{obj.related_name}.all()'):
                    objs.append(obj)
        if len(objs) > 0:
            msg = f'Direccion no se puede inactivar ya que tiene relación con los siguientes objetos: {objs}'
            self.add_error(None, msg)

        if self.has_changed(): 
            self.add_error(None, f'Hubo cambios en los datos del objeto.')

AddressListModelFormSet = forms.modelformset_factory(Address, fields=('code',), extra=0)
