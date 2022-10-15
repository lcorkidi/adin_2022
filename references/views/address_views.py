from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView, GenericActivateView
from references.models import Address
from references.forms.address_forms import AddressDetailModelForm, AddressCreateModelForm, AddressDeleteModelForm, AddressActivateModelForm, AddressListModelFormSet
from references.utils import GetActionsOn, GetIncludedStates

title = Address._meta.verbose_name_plural
ref_urls = { 'list':'references:address_list', 'create':'references:address_create', 'detail':'references:address_detail', 'delete':'references:address_delete', 'activate':'references:address_activate' }

class AddressListView(GenericListView):

    formset = AddressListModelFormSet
    model = Address
    title = title
    ref_urls = ref_urls
    actions_on = GetActionsOn
    list_order = 'code'
    permission_required = 'references.view_address'
    include_states = GetIncludedStates

class AddressCreateView(GenericCreateView):

    form = AddressCreateModelForm
    title = title
    ref_urls = ref_urls
    permission_required = 'references.add_address'

class AddressDetailView(GenericDetailView):

    title = title
    model = Address
    form = AddressDetailModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'references.view_address'

class AddressDeleteView(GenericDeleteView):

    title = title
    model = Address
    form = AddressDeleteModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'references.delete_address'

class AddressActivateView(GenericActivateView):

    title = title
    model = Address
    form = AddressActivateModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'references.activate_address'
    success_url = 'list'