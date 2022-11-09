from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericUpdateView, GenericDeleteView, GenericActivateView
from accountables.forms.lease_realty_forms import Lease_RealtyCreateForm, Lease_RealtyDetailForm, Lease_RealtyUpdateForm, Lease_RealtyAccoutingForm, Lease_RealtyDeleteForm, Lease_RealtyActivateForm, Lease_RealtyListModelFormSet
from accounting.forms.charge_forms import ChargeReceivablePendingFormSet, ChargeListFormSet
from accounting.models import Charge
from accountables.models import Lease_Realty
from accountables.utils.views_data import lease_realty_related_data, lease_realty_main_data, accountable_related_data, GetActionsOn, GetIncludedStates
from accountables.utils.accounting_data import ACCOUNT_RECEIPT_PRIORITY
from accountables.utils.models_func import formsets_data_call
from adin.utils.related_models import related_data_formsets_call

title = Lease_Realty._meta.verbose_name_plural
ref_urls = { 'return':'accountables:lease_realty_main', 'list':'accountables:lease_realty_list', 'create':'accountables:lease_realty_create', 'detail':'accountables:lease_realty_detail', 'update':'accountables:lease_realty_update', 'delete':'accountables:lease_realty_delete', 'activate':'accountables:lease_realty_activate', 'accounting':'accountables:lease_realty_accounting', 'report':'accountables:lease_realty_report' }

class Lease_RealtyMainView(LoginRequiredMixin, PermissionRequiredMixin, View):
    
    template = 'accountables/lease_realty_main.html'
    formsets_data = lease_realty_main_data
    title = 'Contratos Arriendo Inmuebles con Errores'
    ref_urls = ref_urls
    actions_on = GetActionsOn
    list_order = 'code'
    permission_required = 'accountables.view_lease_realty'
    
    def get(self, request):
        formsets = formsets_data_call(self.formsets_data, request.user)
        context = {'formsets': formsets, 'title': self.title, 'ref_urls': self.ref_urls}
        return render(request, self.template, context)

class Lease_RealtyListView(GenericListView):

    formset = Lease_RealtyListModelFormSet
    model = Lease_Realty
    title = title
    ref_urls = ref_urls
    actions_on = GetActionsOn
    list_order = 'code'
    permission_required = 'accountables.view_lease_realty'
    include_states = GetIncludedStates

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
    actions_on = GetActionsOn
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
    actions_on = GetActionsOn
    related_data = lease_realty_related_data
    permission_required = 'accountables.change_lease_realty'
    
class Lease_RealtyAccountingView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'accountables/accountable_accounting.html'
    model = Lease_Realty
    form = Lease_RealtyAccoutingForm
    pending_formset = ChargeReceivablePendingFormSet
    title = title
    subtitle = 'Conceptos Transacciones'
    ref_urls = ref_urls
    readonly_fields = ['code', 'realty', 'doc_date', 'start_date', 'end_date']
    fk_fields = ['realty', 'transaction_type']
    related_data = accountable_related_data
    actions_on = GetActionsOn
    permission_required = 'accountables.change_lease_realty'

    def get(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        if Charge.objects.exclude(state=0).filter(concept__accountable=obj).exists():
            pending_formset = self.pending_formset(initial=obj.charge_receivable(ACCOUNT_RECEIPT_PRIORITY))
        else:
            pending_formset = self.pending_formset()
        actions_on = self.actions_on(request.user, self.model.__name__)
        related_data = related_data_formsets_call(self.related_data, pk, request.user)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'form':form, 'pending_formset':pending_formset, 'related_data':related_data, 'fk_fields': self.fk_fields, 'actions_on': actions_on }
        return render(request, self.template, context)
    
class Lease_RealtyReportView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'accountables/accountable_report.html'
    model = Lease_Realty
    form = Lease_RealtyAccoutingForm
    formset = ChargeListFormSet
    title = title
    subtitle = 'Conceptos Transacciones'
    ref_urls = ref_urls
    readonly_fields = ['code', 'realty', 'doc_date', 'start_date', 'end_date']
    fk_fields = ['realty', 'transaction_type']
    related_data = accountable_related_data
    actions_on = GetActionsOn
    permission_required = 'accountables.change_lease_realty'

    def get(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        formset = self.formset(initial=Charge.report.accountable(obj))
        actions_on = self.actions_on(request.user, self.model.__name__)
        related_data = related_data_formsets_call(self.related_data, pk, request.user)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'form':form, 'formset':formset, 'related_data':related_data, 'fk_fields': self.fk_fields, 'actions_on': actions_on }
        return render(request, self.template, context)

class Lease_RealtyDeleteView(GenericDeleteView):

    title = title
    model = Lease_Realty
    form = Lease_RealtyDeleteForm
    ref_urls = ref_urls
    choice_fields = ['role']
    fk_fields = ['lease', 'person', 'realty']
    related_data = lease_realty_related_data
    actions_on = GetActionsOn
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

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        if not form.is_valid():
            if self.related_data:
                related_data = self.related_data()
                for attr, data in related_data.items():
                    filter_expresion = {}
                    filter_expresion[data['filter_expresion']] = pk
                    formset = data['formset'](queryset=data['class'].objects.filter(**filter_expresion))
                    related_data[attr]['formset'] = formset
            else:
                related_data = None
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'form':form, 'related_data':related_data, 'choice_fields':self.choice_fields, 'fk_fields': self.fk_fields, 'actions_off': self.actions_off , 'group': user_group_str(request.user)}
            return render(request, self.template, context)
        obj.state = 2
        obj.save()
        primary = obj.lease_realty_realty_set.get(primary=True)
        primary.state = 2
        primary.save()
        if obj.lease_realty_person_set.filter(role=3).exists():
            holder = obj.lease_realty_person_set.get(role=3)
            holder.state = 2
            holder.save()
        if obj.lease_realty_person_set.filter(role=1).exists():
            leesse = obj.lease_realty_person_set.get(role=1)
            leesse.state = 2
            leesse.save()
        date_value = obj.date_value.get(date=obj.doc_date)
        date_value.state = 2
        date_value.save()
        if self.success_url != 'list':
            return redirect(self.ref_urls[self.success_url], obj.pk)
        else:
            return redirect(self.ref_urls[self.success_url])
