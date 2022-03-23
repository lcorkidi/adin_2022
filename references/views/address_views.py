from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView, GenericActivateView
from references.models import Address
from references.forms.address_forms import AddressDetailModelForm, AddressCreateModelForm, AddressDeleteModelForm, AddressListModelFormSet

title = Address._meta.verbose_name_plural
ref_urls = { 'list':'references:address_list', 'create':'references:address_create', 'detail':'references:address_detail', 'delete':'references:address_delete', 'activate':'references:address_activate' }

class AddressListView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'references.view_address'

    def get(self, request):
        if request.user.has_perm('references.activate_address'):
            return redirect('references:address_list_all')
        else: 
            return redirect('references:address_list_some')

class AddressListSomeView(GenericListView):

    template = 'adin/generic_list.html'
    formset = AddressListModelFormSet
    model = Address
    title = title
    ref_urls = ref_urls
    actions_off = ['update']
    list_order = 'code'
    permission_required = 'references.view_address'

class AddressListAllView(GenericListView):

    template = 'adin/generic_list.html'
    formset = AddressListModelFormSet
    model = Address
    title = title
    ref_urls = ref_urls
    actions_off = ['update']
    list_order = 'code'
    permission_required = 'references.activate_address'
    include_states = [ 0, 1, 2, 3 ]

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
    form = AddressDeleteModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'references.activate_address'
