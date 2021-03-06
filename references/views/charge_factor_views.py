from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericListView, GenericCreateView, GenericDetailView, GenericUpdateView, GenericDeleteView, GenericActivateView
from references.forms.charge_factor_forms import Charge_FactorCreateForm, Factor_DataCreateForm, Factor_DataDetailForm, Factor_DataDeleteForm, Factor_DataListModelFormSet
from references.models import Factor_Data, Charge_Factor
from home.utils import user_group_str

title = Factor_Data._meta.verbose_name_plural
ref_urls = { 'list':'references:factor_data_list', 'create':'references:charge_factor_create', 'detail':'references:factor_data_detail', 'update':'references:factor_data_update', 'delete':'references:factor_data_delete', 'activate': 'references:factor_data_activate' }

class Factor_DataListView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'references.view_factor_data'

    def get(self, request):
        if request.user.has_perm('references.activate_charge_factor'):
            return redirect('references:factor_data_list_all')
        else: 
            return redirect('references:factor_data_list_some')

class Factor_DataListSomeView(GenericListView):

    template = 'adin/generic_list.html'
    formset = Factor_DataListModelFormSet
    model = Factor_Data
    title = title
    fk_fields = ['factor']
    actions_off = ['update']
    ref_urls = ref_urls
    list_order = 'validity_date'
    permission_required = 'references.view_factor_data'

class Factor_DataListAllView(GenericListView):

    template = 'adin/generic_list.html'
    formset = Factor_DataListModelFormSet
    model = Factor_Data
    title = title
    fk_fields = ['factor']
    actions_off = ['update']
    ref_urls = ref_urls
    list_order = 'validity_date'
    permission_required = 'references.activate_charge_factor'
    include_states = [ 0, 1, 2, 3 ]

class Charge_FactorCreateView(GenericCreateView):

    template = 'references/charge_factor_create.html'
    form = Charge_FactorCreateForm
    title = title
    subtitle = 'Crear o Seleccionar'
    ref_urls = ref_urls
    permission_required = 'references.add_charge_factor'

    def post(self, request):
        form = self.form(request.POST)
        if not form.is_valid():
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user)}
            return render(request, self.template, context)
        form.creator = request.user
        obj = form.save()            
        return redirect('references:factor_data_create', obj.pk)

class Factor_DataCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_create.html'
    form = Factor_DataCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['factor']
    permission_required = 'references.add_factor_data'
    
    def get(self, request, rel_pk):
        obj = Charge_Factor.objects.get(pk=rel_pk)
        form = self.form(initial={'factor': obj})
        if self.readonly_fields:
            form.set_readonly_fields(self.readonly_fields)
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request, rel_pk):
        form = self.form(request.POST)
        if not form.is_valid():
            if self.readonly_fields:
                form.set_readonly_fields(self.readonly_fields)
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user)}
            return render(request, self.template, context)
        form.creator = request.user
        form.save()            
        return redirect(self.ref_urls['list'])

class Factor_DataDetailView(GenericDetailView):

    title = title
    model = Factor_Data
    form = Factor_DataDetailForm
    ref_urls = ref_urls
    fk_fields = [ 'factor' ]
    actions_off = ['update']
    permission_required = 'references.view_factor_data'

class Factor_DataDeleteView(GenericDeleteView):

    title = title
    model = Factor_Data
    form = Factor_DataDeleteForm
    ref_urls = ref_urls
    fk_fields = [ 'factor' ]
    actions_off = ['update']
    permission_required = 'references.delete_factor_data'

class Factor_DataActivateView(GenericActivateView):

    title = title
    model = Factor_Data
    form = Factor_DataDetailForm
    ref_urls = ref_urls
    fk_fields = [ 'factor' ]
    actions_off = ['update']
    permission_required = 'references.activate_charge_factor'
