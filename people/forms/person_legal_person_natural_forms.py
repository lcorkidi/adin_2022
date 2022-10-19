from django.forms import BaseModelFormSet, modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm, GenericDeleteRelatedForm, GenericActivateRelatedForm
from people.models import Person_Legal_Person_Natural

class Person_Legal_Person_NaturalCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Person_Legal_Person_Natural
        exclude = ('state',)

    def clean_person_natural(self):
        person_natural = self.cleaned_data['person_natural']
        if person_natural.state == 0:
            self.add_error('person_natural', f'Personal seleccionado inactivo.')
        return person_natural

class Person_Legal_Person_NaturalUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Person_Legal_Person_Natural
        exclude = ('state',)

class Person_Legal_Person_NaturalDeleteForm(GenericDeleteRelatedForm):

    class Meta:
        model = Person_Legal_Person_Natural
        exclude = ('state',)

class Person_Legal_Person_NaturalActivateForm(GenericActivateRelatedForm):

    related_fields = ['person_natural', 'person_legal']

    class Meta:
        model = Person_Legal_Person_Natural
        exclude = ('state',)

class Person_Legal_Person_NaturalRelatedBaseModelFormSet(BaseModelFormSet):

    def __init__(self, rel_pk, *args, **kwargs):
        super(Person_Legal_Person_NaturalRelatedBaseModelFormSet, self).__init__(*args, **kwargs)

Person_Legal_Person_NaturalModelFormSet = modelformset_factory(Person_Legal_Person_Natural, formset=Person_Legal_Person_NaturalRelatedBaseModelFormSet, fields=('state', 'person_natural', 'appointment'), extra=0)
