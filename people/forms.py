from django import forms
from .models import Person, Person_Natural, Person_Legal, Person_Phone, Person_E_Mail, Person_Address, Person_Legal_Person_Natural
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

class Person_PhoneCreateForm(forms.ModelForm):

    class Meta:
        model = Person_Phone
        fields = '__all__'

    def save(self, *args, **kwargs):
        base_args = {k: self.cleaned_data[k] for k in self.fields}
        base_args['state_change_user'] = self.creator
        per_pho = Person_Phone(**base_args)
        per_pho.save()

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

class Person_EmailCreateForm(forms.ModelForm):

    class Meta:
        model = Person_E_Mail
        fields = '__all__'

    def save(self, *args, **kwargs):
        base_args = {k: self.cleaned_data[k] for k in self.fields}
        base_args['state_change_user'] = self.creator
        per_ema = Person_E_Mail(**base_args)
        per_ema.save()

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

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

class Person_StaffCreateForm(forms.ModelForm):

    class Meta:
        model = Person_Legal_Person_Natural
        fields = '__all__'

    def save(self, *args, **kwargs):
        base_args = {k: self.cleaned_data[k] for k in self.fields}
        base_args['state_change_user'] = self.creator
        per_add = Person_Legal_Person_Natural(**base_args)
        per_add.save()

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

class Person_NaturalDetailForm(forms.ModelForm):

    class Meta:
        model = Person_Natural
        fields = ['type', 'complete_name', 'id_type', 'id_number', 'phone', 'e_mail', 'address']

    def set_hidden_field(self, field):
        self.fields[field].widget.attrs['hidden'] = True
        self.fields[field].required = False

class Person_LegalDetailForm(forms.ModelForm):

    class Meta:
        model = Person_Legal
        fields = ['type', 'complete_name', 'id_type', 'id_number', 'phone', 'e_mail', 'address', 'staff']

    def set_hidden_field(self, field):
        self.fields[field].widget.attrs['hidden'] = True
        self.fields[field].required = False

class Person_NaturalUpdateForm(forms.ModelForm):

    class Meta:
        model = Person_Natural
        fields = ['type', 'name', 'last_name', 'id_type', 'id_number', 'phone', 'e_mail', 'address' ]

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

    def set_hidden_field(self, field):
        self.fields[field].widget.attrs['hidden'] = True
        self.fields[field].required = False


class Person_LegalUpdateForm(forms.ModelForm):

    class Meta:
        model = Person_Legal
        fields = ['type', 'name', 'legal_type', 'id_type', 'id_number', 'phone', 'e_mail', 'address', 'staff' ]

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

    def set_hidden_field(self, field):
        self.fields[field].widget.attrs['hidden'] = True
        self.fields[field].required = False

class Person_PhoneUpdateForm(forms.ModelForm):

    class Meta:
        model = Person_Phone
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
        per_pho = Person_Phone.objects.get(**get_args)
        for k, v in update_args.items():
            setattr(per_pho, k, v)
        per_pho.state_change_date = self.creator
        per_pho.save()

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

class Person_EmailUpdateForm(forms.ModelForm):

    class Meta:
        model = Person_E_Mail
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
        per_ema = Person_E_Mail.objects.get(**get_args)
        for k, v in update_args.items():
            setattr(per_ema, k, v)
        per_ema.state_change_date = self.creator
        per_ema.save()

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

class Person_StaffUpdateForm(forms.ModelForm):

    class Meta:
        model = Person_Legal_Person_Natural
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
        per_add = Person_Legal_Person_Natural.objects.get(**get_args)
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

PersonListModelFormSet = forms.modelformset_factory(Person, fields=('complete_name', 'id_type', 'id_number'), extra=0)
Person_PhoneModelFormSet = forms.modelformset_factory(Person_Phone, fields=('person', 'phone', 'use'), extra=0)
Person_EmailModelFormSet = forms.modelformset_factory(Person_E_Mail, fields=('person', 'e_mail', 'use'), extra=0)
Person_AddressModelFormSet = forms.modelformset_factory(Person_Address, fields=('person', 'address', 'use'), extra=0)
Person_Legal_Person_NaturalModelFormSet = forms.modelformset_factory(Person_Legal_Person_Natural, fields=('person', 'staff', 'appointment'), extra=0)

def person_natural_m2m_data(*args):
    m2m_data = {
        'phone': {
            'class': Person_Phone,
            'formset': Person_PhoneModelFormSet,
            'filter_expresion': 'person__id_number',
            'create_url': 'people:people_phone_create',
            'update_url': 'people:people_phone_update',
            'delete_url': 'people:people_phone_delete'
        },
        'e_mail': {
            'class': Person_E_Mail,
            'formset': Person_EmailModelFormSet,
            'filter_expresion': 'person__id_number',
            'create_url': 'people:people_email_create',
            'update_url': 'people:people_email_update',
            'delete_url': 'people:people_email_delete'
        },
        'address': {
            'class': Person_Address,
            'formset': Person_AddressModelFormSet,
            'filter_expresion': 'person__id_number',
            'create_url': 'people:people_address_create',
            'update_url': 'people:people_address_update',
            'delete_url': 'people:people_address_delete'
        }      
    }
    return m2m_data

def person_legal_m2m_data(*args):
    m2m_data = person_natural_m2m_data()
    m2m_data['staff'] = {
        'class': Person_Legal_Person_Natural,
        'formset': Person_Legal_Person_NaturalModelFormSet,
        'filter_expresion': 'person__id_number',
        'create_url': 'people:people_staff_create',
        'update_url': 'people:people_staff_update',
        'delete_url': 'people:people_staff_delete'
    }        
    return m2m_data

