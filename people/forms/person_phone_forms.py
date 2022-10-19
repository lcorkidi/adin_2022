from django.forms import BaseModelFormSet, modelformset_factory

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

class Person_PhoneRelatedBaseModelFormSet(BaseModelFormSet):

    def __init__(self, rel_pk, *args, **kwargs):
        super(Person_PhoneRelatedBaseModelFormSet, self).__init__(*args, **kwargs)

Person_PhoneModelFormSet = modelformset_factory(Person_Phone, formset=Person_PhoneRelatedBaseModelFormSet, fields=('state', 'phone', 'use'), extra=0)
