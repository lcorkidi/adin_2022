from django.forms import modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm
from accountables.models import Lease_Realty_Realty

class Lease_Realty_RealtyCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Lease_Realty_Realty
        exclude = ('state',)

class Lease_Realty_RealtyUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Lease_Realty_Realty
        exclude = ('state',)

Lease_Realty_RealtyModelFormSet = modelformset_factory(Lease_Realty_Realty, fields=('state',  'realty', 'primary'), extra=0)