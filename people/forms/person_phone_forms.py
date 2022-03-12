from django.forms import modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm
from people.models import Person_Phone

class Person_PhoneCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Person_Phone
        fields = '__all__'

class Person_PhoneUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Person_Phone
        fields = '__all__'

Person_PhoneModelFormSet = modelformset_factory(Person_Phone, fields=('phone', 'use'), extra=0)
