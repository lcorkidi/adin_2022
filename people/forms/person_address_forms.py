from django.forms import BaseModelFormSet, modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm, GenericDeleteRelatedForm, GenericActivateRelatedForm
from people.models import Person_Address

class Person_AddressCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Person_Address
        exclude = ('state',)

    def clean_address(self):
        address = self.cleaned_data['address']
        if address.state == 0:
            self.add_error('address', f'Dirección seleccionada inactiva.')
        return address

class Person_AddressUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Person_Address
        exclude = ('state',)

class Person_AddressDeleteForm(GenericDeleteRelatedForm):

    class Meta:
        model = Person_Address
        exclude = ('state',)

class Person_AddressActivateForm(GenericActivateRelatedForm):

    related_fields = ['person', 'address']

    class Meta:
        model = Person_Address
        exclude = ('state',)

class Person_AddressRelatedBaseModelFormSet(BaseModelFormSet):

    def __init__(self, rel_pk, *args, **kwargs):
        super(Person_AddressRelatedBaseModelFormSet, self).__init__(*args, **kwargs)
                
Person_AddressModelFormSet = modelformset_factory(Person_Address, formset=Person_AddressRelatedBaseModelFormSet, fields=('state', 'address', 'use'), extra=0)
