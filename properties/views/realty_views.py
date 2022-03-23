from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericUpdateView, GenericDeleteView, GenericActivateView
from properties.forms.realty_forms import RealtyCreateForm, RealtyDetailForm, RealtyUpdateForm, RealtyDeleteForm, RealtyListModelFormSet
from properties.models import Realty
from properties.utils import realty_related_data

title = Realty._meta.verbose_name_plural
ref_urls = { 'list':'properties:realty_list', 'create':'properties:realty_create', 'detail':'properties:realty_detail', 'update':'properties:realty_update', 'delete':'properties:realty_delete', 'activate':'properties:realty_activate' }

class RealtyListView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'properties.view_realty'

    def get(self, request):
        if request.user.has_perm('properties.activate_realty'):
            return redirect('properties:realty_list_all')
        else: 
            return redirect('properties:realty_list_some')

class RealtyListSomeView(GenericListView):

    template = 'adin/generic_list.html'
    formset = RealtyListModelFormSet
    model = Realty
    choice_fields = ['use']
    title = title
    ref_urls = ref_urls
    list_order = 'code'
    permission_required = 'properties.view_realty'

class RealtyListAllView(GenericListView):

    template = 'adin/generic_list.html'
    formset = RealtyListModelFormSet
    model = Realty
    choice_fields = ['use']
    title = title
    ref_urls = ref_urls
    list_order = 'code'
    permission_required = 'properties.activate_realty'
    include_states = [ 0, 1, 2, 3 ]

class RealtyCreateView(GenericCreateView):

    template = 'adin/generic_create.html'
    form = RealtyCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    permission_required = 'properties.add_realty'

class RealtyDetailView(GenericDetailView):

    title = title
    model = Realty
    form = RealtyDetailForm
    ref_urls = ref_urls
    choice_fields = ['type', 'use']
    fk_fields = ['address', 'estate']
    related_data = realty_related_data
    permission_required = 'properties.view_realty'

class RealtyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'properties.view_realty'

    def get(self, request, pk):
        if request.user.has_perm('properties.activate_realty'):
            return redirect('properties:realty_update_all', pk)
        else: 
            return redirect('properties:realty_update_some', pk)

class RealtyUpdateSomeView(GenericUpdateView):

    model = Realty
    form = RealtyUpdateForm
    title = title
    ref_urls = ref_urls
    readonly_fields = ['code', 'address']
    choice_fields = ['type', 'use']
    fk_fields = ['address', 'estate']
    related_data = realty_related_data
    permission_required = 'properties.change_realty'

class RealtyUpdateAllView(GenericUpdateView):

    model = Realty
    form = RealtyUpdateForm
    title = title
    ref_urls = ref_urls
    readonly_fields = ['code', 'address']
    choice_fields = ['type', 'use']
    fk_fields = ['address', 'estate']
    related_data = realty_related_data
    permission_required = 'properties.activate_realty'
    include_states = [ 0, 1, 2, 3 ]

class RealtyDeleteView(GenericDeleteView):

    title = title
    model = Realty
    form = RealtyDeleteForm
    ref_urls = ref_urls
    choice_fields = ['type', 'use']
    fk_fields = ['address', 'estate']
    related_data = realty_related_data
    permission_required = 'properties.delete_realty'

class RealtyActivateView(GenericActivateView):

    title = title
    model = Realty
    form = RealtyDeleteForm
    ref_urls = ref_urls
    choice_fields = ['type', 'use']
    fk_fields = ['address', 'estate']
    related_data = realty_related_data
    permission_required = 'properties.activate_realty'
