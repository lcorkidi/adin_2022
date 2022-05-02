from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericUpdateView, GenericDeleteView, GenericActivateView
from properties.forms.estate_forms import EstateCreateForm, EstateDetailForm, EstateUpdateForm, EstateDeleteForm, EstateActivateForm, EstateListModelFormSet
from properties.models import Estate
from properties.utils import estate_related_data

title = Estate._meta.verbose_name_plural
ref_urls = { 'list':'properties:estate_list', 'create':'properties:estate_create', 'detail':'properties:estate_detail', 'update':'properties:estate_update', 'delete':'properties:estate_delete', 'activate':'properties:estate_activate' }

class EstateListView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'properties.view_estate'

    def get(self, request):
        if request.user.has_perm('properties.activate_estate'):
            return redirect('properties:estate_list_all')
        else: 
            return redirect('properties:estate_list_some')

class EstateListSomeView(GenericListView):

    template = 'adin/generic_list.html'
    formset = EstateListModelFormSet
    model = Estate
    choice_fields = ['id_type']
    title = title
    ref_urls = ref_urls
    list_order = 'national_number'
    permission_required = 'properties.view_estate'

class EstateListAllView(GenericListView):

    template = 'adin/generic_list.html'
    formset = EstateListModelFormSet
    model = Estate
    choice_fields = ['id_type']
    title = title
    ref_urls = ref_urls
    list_order = 'national_number'
    permission_required = 'properties.view_estate'
    include_states = [ 0, 1, 2, 3 ]

class EstateCreateView(GenericCreateView):

    template = 'adin/generic_create.html'
    form = EstateCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    permission_required = 'properties.add_estate'

class EstateDetailView(GenericDetailView):

    title = title
    model = Estate
    form = EstateDetailForm
    ref_urls = ref_urls
    choice_fields = ['type']
    fk_fields = ['address', 'person']
    related_data = estate_related_data
    permission_required = 'properties.view_estate'

class EstateUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'properties.change_estate'

    def get(self, request, pk):
        if request.user.has_perm('properties.activate_estate'):
            return redirect('properties:estate_update_all', pk)
        else: 
            return redirect('properties:estate_update_some', pk)

class EstateUpdateSomeView(GenericUpdateView):

    model = Estate
    form = EstateUpdateForm
    title = title
    ref_urls = ref_urls
    readonly_fields = ['national_number']
    choice_fields = ['type']
    fk_fields = ['address', 'person']
    related_data = estate_related_data
    permission_required = 'properties.change_estate'

class EstateUpdateAllView(GenericUpdateView):

    model = Estate
    form = EstateUpdateForm
    title = title
    ref_urls = ref_urls
    readonly_fields = ['national_number']
    choice_fields = ['type']
    fk_fields = ['address', 'person']
    related_data = estate_related_data
    permission_required = 'properties.activate_estate'
    include_states = [ 0, 1, 2, 3 ]

class EstateDeleteView(GenericDeleteView):

    title = title
    model = Estate
    form = EstateDeleteForm
    ref_urls = ref_urls
    choice_fields = ['type']
    fk_fields = ['address', 'person']
    related_data = estate_related_data
    permission_required = 'properties.delete_estate'

class EstateActivateView(GenericActivateView):

    title = title
    model = Estate
    form = EstateActivateForm
    ref_urls = ref_urls
    choice_fields = ['type']
    fk_fields = ['address', 'person']
    related_data = estate_related_data
    permission_required = 'properties.activate_estate'
