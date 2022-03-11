from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView
from references.models import Address
from references.forms.address_forms import AddressDetailModelForm, AddressCreateModelForm, AddressDeleteModelForm, AddressListModelFormSet

title = Address._meta.verbose_name_plural
ref_urls = { 'list':'references:address_list', 'create':'references:address_create', 'detail':'references:address_detail', 'delete':'references:address_delete' }

class AddressListView(GenericListView):

    template = 'adin/generic_list.html'
    formset = AddressListModelFormSet
    model = Address
    title = title
    ref_urls = ref_urls
    actions_off = ['update']
    list_order = 'code'
    permission_required = 'people.view_address'

class AddressCreateView(GenericCreateView):

    form = AddressCreateModelForm
    title = title
    ref_urls = ref_urls
    permission_required = 'people.add_address'

class AddressDetailView(GenericDetailView):

    title = title
    model = Address
    form = AddressDetailModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'people.view_address'

class AddressDeleteView(GenericDeleteView):

    title = title
    model = Address
    form = AddressDeleteModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'people.delete_address'
