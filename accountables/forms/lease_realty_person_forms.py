from django.forms import modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm, GenericDeleteRelatedForm, GenericActivateRelatedForm
from accountables.models import Lease_Realty_Person

class Lease_Realty_PersonCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Lease_Realty_Person
        exclude = ('state',)

class Lease_Realty_PersonUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Lease_Realty_Person
        exclude = ('state',)

class Lease_Realty_PersonDeleteForm(GenericDeleteRelatedForm):

    class Meta:
        model = Lease_Realty_Person
        exclude = ('state',)

class Lease_Realty_PersonActivateForm(GenericActivateRelatedForm):

    related_fields = ['lease', 'person']

    class Meta:
        model = Lease_Realty_Person
        exclude = ('state',)

Lease_Realty_PersonModelFormSet = modelformset_factory(Lease_Realty_Person, fields=('state',  'person', 'role'), extra=0)