from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView, GenericActivateView
from accounting.models import Charge_Concept
from accounting.forms.charge_concept_form import Charge_ConceptDetailModelForm, Charge_ConceptCreateModelForm, Charge_ConceptDeleteModelForm, Charge_ConceptListModelFormSet

title = Charge_Concept._meta.verbose_name_plural
ref_urls = { 'list':'accounting:charge_concept_list', 'create':'accounting:charge_concept_create', 'detail':'accounting:charge_concept_detail', 'delete':'accounting:charge_concept_delete', 'activate':'accounting:charge_concept_activate' }

class Charge_ConceptListView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'accounting.view_charge_concept'

    def get(self, request):
        if request.user.has_perm('accounting.activate_charge'):
            return redirect('accounting:charge_concept_list_all')
        else: 
            return redirect('accounting:charge_concept_list_some')

class Charge_ConceptListSomeView(GenericListView):

    template = 'adin/generic_list.html'
    formset = Charge_ConceptListModelFormSet
    model = Charge_Concept
    title = title
    ref_urls = ref_urls
    actions_off = ['update']
    list_order = 'accountable'
    permission_required = 'accounting.view_charge_concept'

class Charge_ConceptListAllView(GenericListView):

    template = 'adin/generic_list.html'
    formset = Charge_ConceptListModelFormSet
    model = Charge_Concept
    title = title
    ref_urls = ref_urls
    actions_off = ['update']
    list_order = 'accountable'
    permission_required = 'accounting.activate_charge'
    include_states = [ 0, 1, 2, 3 ]

class Charge_ConceptCreateView(GenericCreateView):

    form = Charge_ConceptCreateModelForm
    title = title
    ref_urls = ref_urls
    permission_required = 'accounting.add_charge_concept'

class Charge_ConceptDetailView(GenericDetailView):

    title = title
    model = Charge_Concept
    form = Charge_ConceptDetailModelForm
    ref_urls = ref_urls
    fk_fields = ['accountables', 'transaction_type']
    actions_off = ['update']
    permission_required = 'accounting.view_charge_concept'

class Charge_ConceptDeleteView(GenericDeleteView):

    title = title
    model = Charge_Concept
    form = Charge_ConceptDeleteModelForm
    ref_urls = ref_urls
    fk_fields = ['accountables', 'transaction_type']
    actions_off = ['update']
    permission_required = 'accounting.delete_charge_concept'

class Charge_ConceptActivateView(GenericActivateView):

    title = title
    model = Charge_Concept
    form = Charge_ConceptDeleteModelForm
    ref_urls = ref_urls
    fk_fields = ['accountables', 'transaction_type']
    actions_off = ['update']
    permission_required = 'accounting.activate_charge'
