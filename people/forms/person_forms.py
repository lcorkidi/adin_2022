from django import forms

from people.models import Person, Person_Natural, Person_Legal
from people.utils import personcompletename

class PersonCreateForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['type']

class Person_NaturalCreateForm(forms.ModelForm):

    class Meta:
        model = Person_Natural
        fields = ['type', 'name', 'last_name', 'id_type', 'id_number']

    def clean_type(self):
        field = self.cleaned_data.get('type')
        if field != 0:
            raise forms.ValidationError("Debe ser persona natural.")
        return field

    def clean_id_type(self):
        field = self.cleaned_data.get('id_type')
        if field == 1:
            raise forms.ValidationError("Tipo documento para persona natural no puede ser Nit.")
        return field

    def clean_id_number(self):
        field = self.cleaned_data.get('id_number')
        if Person.objects.filter(pk=field).exists():
            obj = Person.objects.get(pk=field)
            if obj.state == 0:
                raise forms.ValidationError("Persona con número de documento ya existe y está inactiva.")
            else:
                raise forms.ValidationError("Persona con número de documento ya existe y está inactiva.")
        return field

    def save(self, *args, **kwargs):
        base_args = {k: self.cleaned_data[k] for k in self.fields}
        base_args['state_change_user'] = self.creator
        per_nat = Person_Natural(**base_args)
        per_nat.save()
        return per_nat

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

class Person_LegalCreateForm(forms.ModelForm):

    class Meta:
        model = Person_Legal
        fields = ['type', 'name', 'legal_type', 'id_type', 'id_number']

    def clean_type(self):
        field = self.cleaned_data.get('type')
        if field != 1:
            raise forms.ValidationError("Debe ser persona jurídica.")
        return field

    def clean_id_type(self):
        field = self.cleaned_data.get('id_type')
        if field != 1:
            raise forms.ValidationError("Tipo documento para persona jurídica debe ser Nit.")
        return field

    def clean_id_number(self):
        field = self.cleaned_data.get('id_type')
        if Person.objects.filter(pk=field).exists():
            obj = Person.objects.get(pk=field)
            if obj.state == 0:
                raise forms.ValidationError("Persona con número de documento ya existe y está inactiva.")
            else:
                raise forms.ValidationError("Persona con número de documento ya existe y está inactiva.")
        return field

    def save(self, *args, **kwargs):
        base_args = {k: self.cleaned_data[k] for k in self.fields}
        base_args['state_change_user'] = self.creator
        per_leg = Person_Legal(**base_args)
        per_leg.complete_name = personcompletename(per_leg)
        per_leg.save()
        return per_leg

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

class Person_NaturalDetailForm(forms.ModelForm):

    class Meta:
        model = Person_Natural
        fields = ['type', 'complete_name', 'id_type', 'id_number']

class Person_LegalDetailForm(forms.ModelForm):

    class Meta:
        model = Person_Legal
        fields = ['type', 'complete_name', 'id_type', 'id_number']

class Person_NaturalUpdateForm(forms.ModelForm):

    class Meta:
        model = Person_Natural
        fields = ['type', 'name', 'last_name', 'id_type', 'id_number']

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False


class Person_LegalUpdateForm(forms.ModelForm):

    class Meta:
        model = Person_Legal
        fields = ['type', 'name', 'legal_type', 'id_type', 'id_number']

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

class Person_NaturalDeleteForm(forms.ModelForm):

    class Meta:
        model = Person_Natural
        fields = ['type', 'complete_name', 'id_type', 'id_number']

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

class Person_LegalDeleteForm(forms.ModelForm):

    class Meta:
        model = Person_Legal
        fields = ['type', 'complete_name', 'id_type', 'id_number']

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

PersonListModelFormSet = forms.modelformset_factory(Person, fields=('complete_name', 'id_type', 'id_number'), extra=0)
