from django.forms import modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm
from people.models import Person_Legal_Person_Natural

class Person_Legal_Person_NaturalCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Person_Legal_Person_Natural
        exclude = ('state',)

class Person_Legal_Person_NaturalUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Person_Legal_Person_Natural
        exclude = ('state',)

Person_Legal_Person_NaturalModelFormSet = modelformset_factory(Person_Legal_Person_Natural, fields=('state', 'person_natural', 'appointment'), extra=0)
