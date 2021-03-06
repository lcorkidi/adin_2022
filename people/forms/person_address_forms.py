from django.forms import modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm, GenericDeleteRelatedForm, GenericActivateRelatedForm
from people.models import Person_Address

class Person_AddressCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Person_Address
        exclude = ('state',)

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
                
Person_AddressModelFormSet = modelformset_factory(Person_Address, fields=('state', 'address', 'use'), extra=0)
