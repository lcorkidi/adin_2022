from django.forms import modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm, GenericDeleteRelatedForm, GenericActivateRelatedForm
from people.models import Person_Phone

class Person_PhoneCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Person_Phone
        exclude = ('state',)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone.state == 0:
            self.add_error('phone', f'Teléfono seleccionado inactivo.')
        return phone

class Person_PhoneUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Person_Phone
        exclude = ('state',)

class Person_PhoneDeleteForm(GenericDeleteRelatedForm):

    class Meta:
        model = Person_Phone
        exclude = ('state',)

class Person_PhoneActivateForm(GenericActivateRelatedForm):

    related_fields = ['person', 'phone']

    class Meta:
        model = Person_Phone
        exclude = ('state',)

Person_PhoneModelFormSet = modelformset_factory(Person_Phone, fields=('state', 'phone', 'use'), extra=0)
