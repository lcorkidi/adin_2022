from django import forms
from .models import Person, Person_Natural, Person_Legal, Person_Phone, Person_Email, Person_Address
from scripts.utils import personcompletename

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

    def save(self, *args, **kwargs):
        base_args = {k: self.cleaned_data[k] for k in self.fields}
        base_args['state_change_user'] = self.creator
        per_nat = Person_Natural(**base_args)
        per_nat.complete_name = personcompletename(per_nat)
        per_nat.save()

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

    def save(self, *args, **kwargs):
        base_args = {k: self.cleaned_data[k] for k in self.fields}
        base_args['state_change_user'] = self.creator
        per_leg = Person_Legal(**base_args)
        per_leg.complete_name = personcompletename(per_leg)
        per_leg.save()

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

class PersonNaturalUpdateForm(forms.ModelForm):

    class Meta:
        model = Person_Natural
        fields = ['type', 'name', 'last_name', 'id_type', 'id_number', 'phone', 'email', 'address' ]

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

    def set_m2m_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['m2m'] = True
            else: 
                self.fields[field].widget.attrs['m2m'] = False

class PersonLegalUpdateForm(forms.ModelForm):

    class Meta:
        model = Person_Legal
        fields = ['type', 'name', 'legal_type', 'id_type', 'id_number', 'phone', 'email', 'address' ]

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

    def set_m2m_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['m2m'] = True
            else: 
                self.fields[field].widget.attrs['m2m'] = False

PersonListModelFormSet = forms.modelformset_factory(Person, fields=('complete_name', 'id_type', 'id_number'), extra=0)
Person_PhoneModelFormSet = forms.modelformset_factory(Person_Phone, fields=('person', 'phone', 'use'), extra=0)
Person_EmailModelFormSet = forms.modelformset_factory(Person_Email, fields=('person', 'email', 'use'), extra=0)
Person_AddressModelFormSet = forms.modelformset_factory(Person_Address, fields=('person', 'address', 'use'), extra=0)
