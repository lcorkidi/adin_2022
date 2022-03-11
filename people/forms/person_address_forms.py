from django import forms

from people.models import Person_Address

class Person_AddressCreateForm(forms.ModelForm):

    class Meta:
        model = Person_Address
        fields = '__all__'

    def save(self, *args, **kwargs):
        base_args = {k: self.cleaned_data[k] for k in self.fields}
        base_args['state_change_user'] = self.creator
        per_add = Person_Address(**base_args)
        per_add.save()

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

class Person_AddressUpdateForm(forms.ModelForm):

    class Meta:
        model = Person_Address
        fields = '__all__'

    def save(self, *args, **kwargs):
        for delta in self.changed_data:
            if delta in args[0]:
                raise forms.ValidationError('No se puede actualizar con esos cambios.')
        get_args = {}
        update_args = {}
        for k in self.fields:
            if k in args[0]:
                get_args[k] = self.cleaned_data[k]
            elif k in self.changed_data:
                update_args[k] = self.cleaned_data[k]
        per_add = Person_Address.objects.get(**get_args)
        for k, v in update_args.items():
            setattr(per_add, k, v)
        per_add.state_change_date = self.creator
        per_add.save()

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False
                
Person_AddressModelFormSet = forms.modelformset_factory(Person_Address, fields=('person', 'address', 'use'), extra=0)
