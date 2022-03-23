from adin.core.views import GenericCreateRelatedView, GenericUpdateRelatedView, GenericDeleteRelatedView
from accountables.models import Lease_Realty_Realty
from accountables.forms.lease_realty_realty_forms import Lease_Realty_RealtyCreateForm, Lease_Realty_RealtyUpdateForm

title = Lease_Realty_Realty._meta.verbose_name_plural
ref_urls = { 'list':'accountables:lease_realty_list', 'create':'accountables:lease_realty_create', 'detail':'accountables:lease_realty_detail', 'update':'accountables:lease_realty_update', 'delete':'accountables:lease_realty_delete' }
rel_urls = { 'create': 'accountables:lease_realty_realty_create', 'delete': 'accountables:lease_realty_realty_delete', 'update': 'accountables:lease_realty_realty_update' }

class Lease_Realty_RealtyCreateView(GenericCreateRelatedView):

    form = Lease_Realty_RealtyCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['lease']
    fk_fields = ['lease']
    permission_required = 'accountables.add_lease_realty_realty'
    related_fields = ['lease', 'realty']

class Lease_Realty_RealtyUpdateView(GenericUpdateRelatedView):

    model = Lease_Realty_Realty
    form = Lease_Realty_RealtyUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['lease', 'realty']
    fk_fields = ['lease', 'realty']
    permission_required = 'accountables.change_lease_realty_realty'

class Lease_Realty_RealtyDeleteView(GenericDeleteRelatedView):

    model = Lease_Realty_Realty
    form = Lease_Realty_RealtyUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    fk_fields = ['lease', 'realty']
    permission_required = 'accountables.delete_lease_realty_realty'
