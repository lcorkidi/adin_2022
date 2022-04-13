from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView, GenericActivateView
from accounting.models import Ledger
from accounting.forms.ledger_forms import LedgerDetailModelForm, LedgerCreateModelForm, LedgerDeleteModelForm, LedgerListModelFormSet
from accounting.forms.charge_forms import ChargeCreateFormset
from accounting.utils import ledger_related_data
from home.utils import user_group_str

title = Ledger._meta.verbose_name_plural
ref_urls = { 'list':'accounting:ledger_list', 'create':'accounting:ledger_create', 'detail':'accounting:ledger_detail', 'delete':'accounting:ledger_delete', 'activate':'accounting:ledger_activate' }

class LedgerListView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'accounting.view_ledger'

    def get(self, request):
        if request.user.has_perm('accounting.activate_ledger'):
            return redirect('accounting:ledger_list_all')
        else: 
            return redirect('accounting:ledger_list_some')

class LedgerListSomeView(GenericListView):

    formset = LedgerListModelFormSet
    model = Ledger
    title = title
    ref_urls = ref_urls
    fk_fields = ['holder', 'third_party']
    actions_off = ['update']
    list_order = 'code'
    permission_required = 'accounting.view_ledger'

class LedgerListAllView(GenericListView):

    formset = LedgerListModelFormSet
    model = Ledger
    title = title
    ref_urls = ref_urls
    fk_fields = ['holder', 'third_party']
    actions_off = ['update']
    list_order = 'code'
    permission_required = 'accounting.activate_ledger'
    include_states = [ 0, 1, 2, 3 ]

class LedgerCreateView(GenericCreateView):

    template = 'accounting/ledger_create.html'
    form = LedgerCreateModelForm
    formset = ChargeCreateFormset
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    permission_required = 'accounting.add_ledger'
    
    def get(self, request):
        form = self.form()
        formset = self.formset()
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'form':form, 'formset': formset, 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request):
        form = self.form(request.POST)
        formset = self.formset(request.POST)
        if not form.is_valid() or not formset.is_valid():
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'form':form, 'formset': formset, 'group': user_group_str(request.user)}
            return render(request, self.template, context)
        form.creator = request.user
        ledger = form.save()            
        formset.creator = request.user
        formset.save(ledger)
        return redirect(self.ref_urls['list'])

class LedgerDetailView(GenericDetailView):

    title = title
    model = Ledger
    form = LedgerDetailModelForm
    ref_urls = ref_urls
    fk_fields = ['holder', 'third_party']
    actions_off = ['update']
    related_data = ledger_related_data
    permission_required = 'accounting.view_ledger'

class LedgerDeleteView(GenericDeleteView):

    title = title
    model = Ledger
    form = LedgerDeleteModelForm
    ref_urls = ref_urls
    fk_fields = ['holder', 'third_party']
    actions_off = ['update']
    related_data = ledger_related_data
    permission_required = 'accounting.delete_ledger'

class LedgerActivateView(GenericActivateView):

    title = title
    model = Ledger
    form = LedgerDeleteModelForm
    ref_urls = ref_urls
    fk_fields = ['holder', 'third_party']
    actions_off = ['update']
    related_data = ledger_related_data
    permission_required = 'accounting.activate_ledger'
