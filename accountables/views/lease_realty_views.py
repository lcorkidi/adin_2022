from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericUpdateView, GenericDeleteView, GenericActivateView
from accountables.forms.lease_realty_forms import Lease_RealtyCreateForm, Lease_RealtyDetailForm, Lease_RealtyUpdateForm, Lease_RealtyDeleteForm, Lease_RealtyActivateForm, Lease_RealtyListModelFormSet
from accountables.models import Lease_Realty
from accountables.utils import lease_realty_related_data

title = Lease_Realty._meta.verbose_name_plural
ref_urls = { 'list':'accountables:lease_realty_list', 'create':'accountables:lease_realty_create', 'detail':'accountables:lease_realty_detail', 'update':'accountables:lease_realty_update', 'delete':'accountables:lease_realty_delete', 'activate':'accountables:lease_realty_activate'  }

class Lease_RealtyListView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'accountables.view_lease_realty'

    def get(self, request):
        if request.user.has_perm('accountables.activate_lease_realty'):
            return redirect('accountables:lease_realty_list_all')
        else: 
            return redirect('accountables:lease_realty_list_some')

class Lease_RealtyListSomeView(GenericListView):

    template = 'adin/generic_list.html'
    formset = Lease_RealtyListModelFormSet
    model = Lease_Realty
    title = title
    ref_urls = ref_urls
    list_order = 'code'
    permission_required = 'accountables.view_lease_realty'

class Lease_RealtyListAllView(GenericListView):

    template = 'adin/generic_list.html'
    formset = Lease_RealtyListModelFormSet
    model = Lease_Realty
    title = title
    ref_urls = ref_urls
    list_order = 'code'
    permission_required = 'accountables.activate_lease_realty'
    include_states = [ 0, 1, 2, 3 ]

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

class Lease_RealtyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'accountables.change_lease_realty'

    def get(self, request, pk):
        if request.user.has_perm('accountables.activate_lease_realty'):
            return redirect('accountables:lease_realty_update_all', pk)
        else: 
            return redirect('accountables:lease_realty_update_some', pk)

class Lease_RealtyUpdateSomeView(GenericUpdateView):

    model = Lease_Realty
    form = Lease_RealtyUpdateForm
    title = title
    ref_urls = ref_urls
    readonly_fields = ['code', 'doc_date']
    choice_fields = ['role']
    fk_fields = ['lease', 'person', 'realty']
    related_data = lease_realty_related_data
    permission_required = 'accountables.change_lease_realty'

class Lease_RealtyUpdateAllView(GenericUpdateView):

    model = Lease_Realty
    form = Lease_RealtyUpdateForm
    title = title
    ref_urls = ref_urls
    readonly_fields = ['code', 'doc_date']
    choice_fields = ['role']
    fk_fields = ['lease', 'person', 'realty']
    related_data = lease_realty_related_data
    permission_required = 'accountables.activate_lease_realty'
    include_states = [ 0, 1, 2, 3 ]

class Lease_RealtyDeleteView(GenericDeleteView):

    title = title
    model = Lease_Realty
    form = Lease_RealtyDeleteForm
    ref_urls = ref_urls
    choice_fields = ['role']
    fk_fields = ['lease', 'person', 'realty']
    related_data = lease_realty_related_data
    permission_required = 'accountables.delete_lease_realty'

class Lease_RealtyActivateView(GenericActivateView):

    title = title
    model = Lease_Realty
    form = Lease_RealtyActivateForm
    ref_urls = ref_urls
    choice_fields = ['role']
    fk_fields = ['lease', 'person', 'realty']
    related_data = lease_realty_related_data
    permission_required = 'accountables.activate_lease_realty'
