from django.forms import Form, ModelChoiceField, TypedChoiceField, modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm, GenericDeleteRelatedForm, GenericActivateRelatedForm
from accountables.models import Lease_Realty_Person, Lease_Realty
from references.models import Phone, E_Mail, Address
from people.models import Person

class Lease_Realty_PersonCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Lease_Realty_Person
        exclude = ('state',)

    def __init__(self, *args, **kwargs):
        super(Lease_Realty_PersonCreateForm, self).__init__(*args, **kwargs)
        self.fields['phone'].required = False
        self.fields['e_mail'].required = False

    def clean_person(self):
        person = self.cleaned_data['person']
        if person.state == 0:
            self.add_error('person', f'Persona seleccionada inactiva.')
        return person

    def clean_role(self):
        lease = self.cleaned_data['lease']
        role = self.cleaned_data['role']
        if role in [1,3] and lease.lease_realty_person_set.exclude(state=0).filter(role=role).exists():
            self.add_error('role', f"{lease.lease_realty_person_set.exclude(state=0).get(role=role).person} ya tiene este rol unico.")
        return role

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone and phone.state == 0:
            self.add_error('phone', f'Teléfono seleccionado inactivo.')
        return phone

    def clean_e_mail(self):
        e_mail = self.cleaned_data['e_mail']
        if e_mail and e_mail.state == 0:
            self.add_error('e_mail', f'Correo seleccionado inactivo.')
        return e_mail

    def clean_address(self):
        address = self.cleaned_data['address']
        if address and address.state == 0:
            self.add_error('address', f'Dirección seleccionada inactiva.')
        return address

class Lease_Realty_PersonUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Lease_Realty_Person
        exclude = ('state',)

    def __init__(self, *args, **kwargs):
        super(Lease_Realty_PersonUpdateForm, self).__init__(*args, **kwargs)
        self.fields['phone'].required = False
        self.fields['e_mail'].required = False

    def clean_role(self):
        lease = self.cleaned_data['lease']
        person = self.cleaned_data['person']
        role = self.cleaned_data['role']
        if role in [1,3] and lease.lease_realty_person_set.exclude(state=0).exclude(person=person).filter(role=role).exists():
            self.add_error('role', f"{lease.lease_realty_person_set.exclude(state=0).get(role=role).person} ya tiene este rol unico.")
        return role

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone and phone.state == 0:
            self.add_error('phone', f'Teléfono seleccionado inactivo.')
        return phone

    def clean_e_mail(self):
        e_mail = self.cleaned_data['e_mail']
        if e_mail and e_mail.state == 0:
            self.add_error('e_mail', f'Correo seleccionado inactivo.')
        return e_mail

    def clean_address(self):
        address = self.cleaned_data['address']
        if address and address.state == 0:
            self.add_error('address', f'Dirección seleccionada inactiva.')
        return address

class ModelChoiceFieldManual(ModelChoiceField):

    def to_python(self, value):
        if value == 'None':
            value = None
        return value

class TypedChoiceFieldManual(TypedChoiceField):

    def to_python(self, value):
        if isinstance(value, str):
            value = int(value)
        return value

class Lease_Realty_PersonDeleteForm(Form):

    ROLE_CHOICE = [
        ('', '----'),
        (0,'Arrendador'),
        (1,'Arrendatario'),
        (2,'Fiador'),
        (3,'Arrendador Titular')
    ]

    lease = ModelChoiceField(
        queryset=Lease_Realty.active.all(),
        label='Contrato:'
    )
    person = ModelChoiceField(
        queryset=Person.active.all(),
        label='Persona:'
    )
    role = TypedChoiceFieldManual(
        choices=ROLE_CHOICE,
        empty_value='',
        initial='',
        label='Rol:'
    )
    phone = ModelChoiceFieldManual(
        queryset=Phone.active.all(),
        required=False,
        blank=True,
        empty_label='None',
        label='Teléfono:'
    )
    e_mail = ModelChoiceFieldManual(
        queryset=E_Mail.active.all(),
        required=False,
        blank=True,
        empty_label='None',
        label='Correo Electrónico:'
    )
    address = ModelChoiceField(
        queryset=Address.active.all(),
        label='Dirección:'
    )

    def clean_role(self):
        role = self.cleaned_data['role']
        if role == self.initial['role']:
            self.fields['role'].error_messages.clear()
            if 'role' in self.changed_data:
                self.changed_data.remove('role')
        return role

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone == self.initial['phone']:
            self.fields['phone'].error_messages.clear()
            if 'phone' in self.changed_data:
                self.changed_data.remove('phone')
        return phone

    def clean_e_mail(self):
        e_mail = self.cleaned_data['e_mail']
        if e_mail == self.initial['e_mail']:
            self.fields['e_mail'].error_messages.clear()
            if 'e_mail' in self.changed_data:
                self.changed_data.remove('e_mail')
        return e_mail

    def clean(self):
        if self.has_changed():
            self.add_error(None, f'Hubo cambios en los datos inmutables del objeto.')
        return super().clean()

class Lease_Realty_PersonActivateForm(Form):

    ROLE_CHOICE = [
        ('', '----'),
        (0,'Arrendador'),
        (1,'Arrendatario'),
        (2,'Fiador'),
        (3,'Arrendador Titular')
    ]

    lease = ModelChoiceField(
        queryset=Lease_Realty.active.all(),
        label='Contrato:'
    )
    person = ModelChoiceField(
        queryset=Person.active.all(),
        label='Persona:'
    )
    role = TypedChoiceFieldManual(
        choices=ROLE_CHOICE,
        empty_value='',
        initial='',
        label='Rol:'
    )
    phone = ModelChoiceFieldManual(
        queryset=Phone.active.all(),
        required=False,
        blank=True,
        empty_label='None',
        label='Teléfono:'
    )
    e_mail = ModelChoiceFieldManual(
        queryset=E_Mail.active.all(),
        required=False,
        blank=True,
        empty_label='None',
        label='Correo Electrónico:'
    )
    address = ModelChoiceField(
        queryset=Address.active.all(),
        label='Dirección:'
    )

    def clean_person(self):
        person = self.cleaned_data['person']
        if person.state == 0:
            self.add_error('person', f'Persona seleccionada inactiva.')
        return person

    def clean_role(self):
        lease = self.cleaned_data['lease']
        person = self.cleaned_data['person']
        role = self.cleaned_data['role']
        role = self.cleaned_data['role']
        if role == self.initial['role']:
            self.fields['role'].error_messages.clear()
            if 'role' in self.changed_data:
                self.changed_data.remove('role')
        if role in [1,3] and lease.lease_realty_person_set.exclude(state=0).exclude(person=person).filter(role=role).exists():
            self.add_error('role', f"{lease.lease_realty_person_set.exclude(state=0).get(role=role).person} ya tiene este rol unico.")
        return role

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone = self.cleaned_data['phone']
        if phone == self.initial['phone']:
            self.fields['phone'].error_messages.clear()
            if 'phone' in self.changed_data:
                self.changed_data.remove('phone')
        if phone and phone.state == 0:
            self.add_error('phone', f'Teléfono seleccionado inactivo.')
        return phone

    def clean_e_mail(self):
        e_mail = self.cleaned_data['e_mail']
        e_mail = self.cleaned_data['e_mail']
        if e_mail == self.initial['e_mail']:
            self.fields['e_mail'].error_messages.clear()
            if 'e_mail' in self.changed_data:
                self.changed_data.remove('e_mail')
        if e_mail and e_mail.state == 0:
            self.add_error('e_mail', f'Correo seleccionado inactivo.')
        return e_mail

    def clean_address(self):
        address = self.cleaned_data['address']
        if address and address.state == 0:
            self.add_error('address', f'Dirección seleccionada inactiva.')
        return address

    def clean(self):
        if self.has_changed():
            self.add_error(None, f'Hubo cambios en los datos inmutables del objeto.')
        return super().clean()

Lease_Realty_PersonModelFormSet = modelformset_factory(Lease_Realty_Person, fields=('state', 'person', 'role'), extra=0)