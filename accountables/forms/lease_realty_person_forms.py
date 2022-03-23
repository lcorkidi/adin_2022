from django.forms import modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm
from accountables.models import Lease_Realty_Person

class Lease_Realty_PersonCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Lease_Realty_Person
        fields = '__all__'

class Lease_Realty_PersonUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Lease_Realty_Person
        fields = '__all__'

Lease_Realty_PersonModelFormSet = modelformset_factory(Lease_Realty_Person, fields=( 'person', 'role'), extra=0)