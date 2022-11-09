from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView, GenericActivateView
from accounting.models import Ledger_Template
from accountables.models import Accountable, Accountable_Concept
from accountables.utils.accounting_data import ACCOUNT_RECEIPT_PRIORITY
from accountables.forms.accountable_forms import AccountableAccoutingForm
from accounting.forms.ledger_template_forms import Ledger_TemplateDetailModelForm, Ledger_TemplateCreateModelForm, Ledger_TemplateDeleteModelForm, Ledger_TemplateSelectForm, Ledger_TemplateSelectAccountableForm, Ledger_TemplateConceptDataForm, Ledger_TemplateSelectConceptForm, Ledger_TemplateListModelFormSet, Ledger_TemplateBulkPendingCreateFormSet
from accounting.forms.charge_template_forms import Charge_TemplateCreateFormset
from accounting.forms.charge_forms import ChargeReceivablePendingFormSet
from accounting.utils import ledger_template_related_data, GetIncludedStates, GetActionsOn
from adin.utils.user_data import user_group_str

title = Ledger_Template._meta.verbose_name_plural
ref_urls = { 'list':'accounting:ledger_template_list', 'create':'accounting:ledger_template_create', 'detail':'accounting:ledger_template_detail', 'delete':'accounting:ledger_template_delete', 'activate':'accounting:ledger_template_activate' }

class Ledger_TemplateListView(GenericListView):

    formset = Ledger_TemplateListModelFormSet
    model = Ledger_Template
    title = title
    ref_urls = ref_urls
    fk_fields = ['transaction_type', 'ledger_type', 'accountable_class']
    actions_on = GetActionsOn
    list_order = 'code'
    permission_required = 'accounting.view_ledger_template'
    include_states = GetIncludedStates

class Ledger_TemplateCreateView(GenericCreateView):

    template = 'accounting/ledger_create.html'
    form = Ledger_TemplateCreateModelForm
    formset = Charge_TemplateCreateFormset
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    permission_required = 'accounting.add_ledger_template'
    
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
        ledger_template = form.save(creator_user=request.user)            
        formset.save(ledger_template, creator_user=request.user)
        return redirect(self.ref_urls['list'])

class Ledger_TemplateDetailView(GenericDetailView):

    title = title
    model = Ledger_Template
    form = Ledger_TemplateDetailModelForm
    ref_urls = ref_urls
    fk_fields = ['transaction_type', 'ledger_type', 'accountable_class']
    choice_fields = ['nature']
    actions_on = GetActionsOn
    related_data = ledger_template_related_data
    permission_required = 'accounting.view_ledger_template'

class Ledger_TemplateDeleteView(GenericDeleteView):

    title = title
    model = Ledger_Template
    form = Ledger_TemplateDeleteModelForm
    ref_urls = ref_urls
    fk_fields = ['transaction_type', 'ledger_type']
    choice_fields = ['nature']
    actions_on = GetActionsOn
    related_data = ledger_template_related_data
    permission_required = 'accounting.delete_ledger_template'

class Ledger_TemplateActivateView(GenericActivateView):

    title = title
    model = Ledger_Template
    form = Ledger_TemplateDeleteModelForm
    ref_urls = ref_urls
    fk_fields = ['transaction_type', 'ledger_type']
    choice_fields = ['nature']
    actions_on = GetActionsOn
    related_data = ledger_template_related_data
    permission_required = 'accounting.activate_ledger_template'

class Ledger_TemplateSelectView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_create.html'
    form = Ledger_TemplateSelectForm
    title = title
    subtitle = 'Escoger Formato'
    ref_urls = ref_urls
    permission_required = 'accounting.add_ledger'

    def get(self, request):
        form = self.form()
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request):
        form = self.form(request.POST)
        if not form.is_valid():
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user)}
            return render(request, self.template, context)
        return redirect('accounting:ledger_template_select_accountable', form['ledger_template'].value())

class Ledger_TemplateSelectAccountableView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_create.html'
    form = Ledger_TemplateSelectAccountableForm
    title = title
    subtitle = 'Escoger Contabilizable'
    ref_urls = ref_urls
    permission_required = 'accounting.add_ledger'
    readonly_fields = ['ledger_template']
    choice_fields = ['ledger_template']

    def get(self, request, pk):
        obj = Ledger_Template.active.get(pk=pk)
        form = self.form(initial={'ledger_template':obj})
        form.set_readonly_fields(self.readonly_fields)
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user), 'choice_fields':self.choice_fields}
        return render(request, self.template, context)

    def post(self, request, pk):
        obj = Ledger_Template.active.get(pk=pk)
        form = self.form(request.POST, initial={'ledger_template':obj})
        if not form.is_valid():
            form.set_readonly_fields(self.readonly_fields)
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user), 'choice_fields':self.choice_fields}
            return render(request, self.template, context)
        if form.concept_dependant():
            return redirect('accounting:ledger_template_select_concept', form['ledger_template'].value(), form['accountable'].value())
        else:
            return redirect('accounting:ledger_template_concept_data', form['ledger_template'].value(), form['accountable'].value())
 
class Ledger_TemplateSelectConceptDataView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_create.html'
    form = Ledger_TemplateConceptDataForm
    title = title
    subtitle = 'Crear Registro'
    ref_urls = ref_urls
    permission_required = 'accounting.add_ledger'
    readonly_fields = ['ledger_template', 'accountable', 'accountable_concept']
    choice_fields = ['ledger_template', 'accountable', 'accountable_concept']

    def get(self, request, lt_pk, acc_pk):
        lt = Ledger_Template.active.get(pk=lt_pk)
        acc = Accountable.active.get(pk=acc_pk)
        acc_con = acc.accountable_concept.filter(transaction_type=lt.transaction_type).earliest()
        form = self.form(initial={'ledger_template':lt, 'accountable':acc, 'accountable_concept':acc_con})
        form.set_readonly_fields(self.readonly_fields)
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user), 'choice_fields':self.choice_fields}
        return render(request, self.template, context)

    def post(self, request, lt_pk, acc_pk):
        lt = Ledger_Template.active.get(pk=lt_pk)
        acc = Accountable.active.get(pk=acc_pk)
        form = self.form(request.POST, initial={'ledger_template':lt, 'accountable':acc})
        if not form.is_valid():
            form.set_readonly_fields(self.readonly_fields)
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user), 'choice_fields':self.choice_fields}
            return render(request, self.template, context)
        form.creator = request.user
        ledger = form.save()    
        return redirect('accounting:ledger_detail', ledger.pk)
 
class Ledger_TemplateSelectConceptView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_create.html'
    form = Ledger_TemplateSelectConceptForm
    title = title
    subtitle = 'Crear Registro'
    ref_urls = ref_urls
    permission_required = 'accounting.add_ledger'
    readonly_fields = ['ledger_template', 'accountable', 'accountable_concept']
    choice_fields = ['ledger_template', 'accountable', 'accountable_concept']

    def get(self, request, lt_pk, acc_pk):
        lt = Ledger_Template.active.get(pk=lt_pk)
        acc = Accountable.active.get(pk=acc_pk)
        acc_con = Accountable_Concept.pending.ledger(acc, lt).earliest('date')
        form = self.form(initial={'ledger_template':lt, 'accountable':acc, 'accountable_concept':acc_con})
        form.set_readonly_fields(self.readonly_fields)
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user), 'choice_fields':self.choice_fields}
        return render(request, self.template, context)

    def post(self, request, lt_pk, acc_pk):
        lt = Ledger_Template.active.get(pk=lt_pk)
        acc = Accountable.active.get(pk=acc_pk)
        acc_con = Accountable_Concept.pending.ledger(acc, lt).earliest('date')
        form = self.form(request.POST, initial={'ledger_template':lt, 'accountable':acc, 'accountable_concept':acc_con})
        if not form.is_valid():
            form.set_readonly_fields(self.readonly_fields)
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user), 'choice_fields':self.choice_fields}
            return render(request, self.template, context)
        ledger = form.save(request.user)    
        return redirect('accounting:ledger_detail', ledger.pk)
 
class Ledger_TemplateRegisterCommitView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_create.html'
    form = Ledger_TemplateSelectConceptForm
    title = title
    subtitle = 'Crear Registro'
    ref_urls = ref_urls
    permission_required = 'accounting.add_ledger'
    readonly_fields = ['ledger_template', 'accountable_concept','ledger_type', 'accountable', 'holder', 'third_party', 'concept_date', 'concept_value']
    choice_fields = ['ledger_template', 'accountable_concept', 'ledger_type', 'accountable', 'holder', 'third_party']

    def get(self, request, ac_pk, lt_str):
        acc_con = Accountable_Concept.active.get(pk=ac_pk)
        acc = acc_con.accountable
        acc_tra_typ = acc_con.accountable.accountable_transaction_type.get(transaction_type=acc_con.transaction_type)
        if lt_str == 'CA':
            lt = acc_tra_typ.commit_template
        elif lt_str == 'FV':
            lt = acc_tra_typ.bill_template
        else:
            lt = acc_tra_typ.receive_template
        form = self.form(initial={'ledger_template':lt, 'accountable_concept':acc_con, 'ledger_type':lt.ledger_type, 'accountable':acc, 'holder':acc.ledger_holder(), 'third_party':acc.ledger_third_party, 'concept_date':acc_con.date, 'concept_value':acc_con.value})
        form.set_readonly_fields(self.readonly_fields)
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user), 'choice_fields':self.choice_fields}
        return render(request, self.template, context)

    def post(self, request, ac_pk, lt_str):
        acc_con = Accountable_Concept.active.get(pk=ac_pk)
        acc = acc_con.accountable
        acc_tra_typ = acc_con.accountable.accountable_transaction_type.get(transaction_type=acc_con.transaction_type)
        if lt_str == 'CA':
            lt = acc_tra_typ.commit_template
        elif lt_str == 'FV':
            lt = acc_tra_typ.bill_template
        else:
            lt = acc_tra_typ.receive_template
        form = self.form(request.POST, initial={'ledger_template':lt, 'accountable_concept':acc_con, 'ledger_type':lt.ledger_type, 'accountable':acc, 'holder':acc.ledger_holder(), 'third_party':acc.ledger_third_party, 'concept_date':acc_con.date, 'concept_value':acc_con.value})
        if not form.is_valid():
            form.set_readonly_fields(self.readonly_fields)
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user), 'choice_fields':self.choice_fields}
            return render(request, self.template, context)
        ledger = form.save(request.user)    
        return redirect('accounting:ledger_detail', ledger.pk)
 
class Ledger_TemplateBulkPendingRegisterView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'accounting/ledger_template_bulk_pending_create.html'
    formset = Ledger_TemplateBulkPendingCreateFormSet
    title = title
    subtitle = 'Crear Registros'
    ref_urls = ref_urls
    permission_required = 'accounting.add_ledger'
    hidden_fields = ['accountable_concept']
    readonly_fields = ['ledger_template', 'accountable_concept','ledger_type', 'accountable', 'holder', 'third_party', 'concept_date', 'concept_value']
    choice_fields = ['ledger_template', 'accountable_concept', 'ledger_type', 'accountable', 'holder', 'third_party']

    def get(self, request, typ_abr):
        formset = self.formset(initial=Accountable_Concept.pending.ledger_type_dict(typ_abr))
        context = {'formset': formset, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields':self.choice_fields, 'hidden_fields':self.hidden_fields}
        return render(request, self.template, context)

    def post(self, request, typ_abr):
        formset = self.formset(request.POST, initial=Accountable_Concept.pending.ledger_type_dict(typ_abr))
        if not formset.is_valid():
            context = {'formset': formset, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user), 'choice_fields':self.choice_fields}
            return render(request, self.template, context)
        formset.save(request.user)    
        return redirect('accountables:lease_realty_main')
 
 
class Ledger_TemplateRegisterReceiptView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'accounting/accountable_receipt.html'
    form = AccountableAccoutingForm
    pending_formset = ChargeReceivablePendingFormSet
    title = title
    subtitle = 'Crear Registro'
    ref_urls = ref_urls
    permission_required = 'accounting.add_ledger'
    readonly_fields = ['ledger_template', 'accountable', 'accountable_concept']
    choice_fields = ['ledger_template', 'accountable', 'accountable_concept']

    def get(self, request, ac_pk):
        acc = Accountable.active.get(pk=ac_pk)
        form = self.form(instance=acc)
        pending_formset = self.pending_formset(initial=acc.subclass_obj().charge_receivable(ACCOUNT_RECEIPT_PRIORITY))
        context = {'form': form, 'pending_formset':pending_formset, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user), 'choice_fields':self.choice_fields}
        return render(request, self.template, context)
