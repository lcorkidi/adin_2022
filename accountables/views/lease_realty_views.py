from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericUpdateView, GenericDeleteView
from accountables.forms.lease_realty_forms import Lease_RealtyCreateForm, Lease_RealtyDetailForm, Lease_RealtyUpdateForm, Lease_RealtyDeleteForm, Lease_RealtyListModelFormSet
from accountables.models import Lease_Realty
from accountables.utils import lease_realty_related_data

title = Lease_Realty._meta.verbose_name_plural
ref_urls = { 'list':'accountables:lease_realty_list', 'create':'accountables:lease_realty_create', 'detail':'accountables:lease_realty_detail', 'update':'accountables:lease_realty_update', 'delete':'accountables:lease_realty_delete' }

class Lease_RealtyListView(GenericListView):

    template = 'adin/generic_list.html'
    formset = Lease_RealtyListModelFormSet
    model = Lease_Realty
    title = title
    ref_urls = ref_urls
    list_order = 'code'
    permission_required = 'accountables.view_lease_realty'

class Lease_RealtyCreateView(GenericCreateView):

    template = 'adin/generic_create.html'
    form = Lease_RealtyCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    permission_required = 'accountables.add_lease_realty'

class Lease_RealtyDetailView(GenericDetailView):

    title = title
    model = Lease_Realty
    form = Lease_RealtyDetailForm
    ref_urls = ref_urls
    choice_fields = ['role']
    fk_fields = ['lease', 'person', 'realty']
    related_data = lease_realty_related_data
    permission_required = 'accountables.view_lease_realty'

class Lease_RealtyUpdateView(GenericUpdateView):

    model = Lease_Realty
    form = Lease_RealtyUpdateForm
    title = title
    ref_urls = ref_urls
    readonly_fields = ['code', 'doc_date']
    choice_fields = ['role']
    fk_fields = ['lease', 'person', 'realty']
    related_data = lease_realty_related_data
    permission_required = 'accountables.change_lease_realty'

class Lease_RealtyDeleteView(GenericDeleteView):

    title = title
    model = Lease_Realty
    form = Lease_RealtyDeleteForm
    ref_urls = ref_urls
    choice_fields = ['role']
    fk_fields = ['lease', 'person', 'realty']
    related_data = lease_realty_related_data
    permission_required = 'accountables.delete_lease_realty'
