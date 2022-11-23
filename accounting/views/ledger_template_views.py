import datetime
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView, GenericActivateView
from accounting.models import Ledger_Template, Ledger_Type
from accountables.models import Accountable, Accountable_Concept
from accountables.utils.accounting_data import ACCOUNT_RECEIPT_PRIORITY
from accountables.forms.accountable_forms import AccountableAccountingForm
from accounting.forms.ledger_forms import LedgerCreateModelForm
from accounting.forms.ledger_template_forms import Ledger_TemplateDetailModelForm, Ledger_TemplateCreateModelForm, Ledger_TemplateDeleteModelForm, Ledger_TemplateActivateModelForm, Ledger_TemplateSelectForm, Ledger_TemplateSelectAccountableForm, Ledger_TemplateConceptDataForm, Ledger_TemplateSelectConceptForm, Ledger_TemplateCodeModelForm, Ledger_TemplateListModelFormSet, Ledger_TemplateBulkPendingCreateFormSet
from accounting.forms.charge_template_forms import Charge_TemplateCreateFormset
from accounting.forms.charge_forms import ChargeReceivablePendingFormSet, ChargeAutoCreateFormset, ChargeCreate4AccountableFormset
from accounting.utils.views_data import ledger_template_related_data, GetIncludedStates, GetActionsOn
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
    form = Ledger_TemplateActivateModelForm
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

    template = 'accounting/ledger_create.html'
    form = LedgerCreateModelForm
    formset = ChargeAutoCreateFormset
    title = title
    subtitle = 'Crear Registro'
    ref_urls = ref_urls
    permission_required = 'accounting.add_ledger'
    readonly_fields = ['type', 'holder', 'third_party', 'account', 'concept', 'debit', 'credit']
    choice_fields = ['type', 'holder', 'third_party']

    def get(self, request, ac_pk, lt_str):
        acc_con = Accountable_Concept.active.get(pk=ac_pk)
        acc = acc_con.accountable
        lt = acc_con.get_applicable_ledger_template(acc_con.transaction_type, lt_str, acc_con.date)
        form = self.form(initial={'type':lt.ledger_type, 'holder':acc.ledger_holder(), 'third_party':acc.ledger_third_party(), 'date':datetime.date.today()})
        form.set_readonly_fields(self.readonly_fields)
        formset_data = []
        for cha_tem in lt.charges_templates.all():
            cha_dat = {}
            cha_dat['account'] = cha_tem.account
            cha_dat['concept'] = acc_con
            cha_dat['debit' if cha_tem.nature == 1 else 'credit'] = abs(cha_tem.factor.factored_value(acc_con.accountable, acc_con.date, acc_con.value, cha_tem.nature))
            cha_dat['credit' if cha_tem.nature == 1 else 'debit'] = 0
            formset_data.append(cha_dat)
        formset = self.formset(initial=formset_data)
        context = {'form': form, 'formset':formset, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields':self.choice_fields, 'acc_pk':acc.pk, 'readonly_fields':self.readonly_fields}
        return render(request, self.template, context)

    def post(self, request, ac_pk, lt_str):
        acc_con = Accountable_Concept.active.get(pk=ac_pk)
        acc = acc_con.accountable
        lt = acc_con.get_applicable_ledger_template(acc_con.transaction_type, lt_str, acc_con.date)
        form = self.form(request.POST, initial={'type':lt.ledger_type, 'holder':acc.ledger_holder(), 'third_party':acc.ledger_third_party(), 'date':datetime.date.today()})
        formset_data = []
        for cha_tem in lt.charges_templates.all():
            cha_dat = {}
            cha_dat['account'] = cha_tem.account
            cha_dat['concept'] = acc_con
            cha_dat['debit' if cha_tem.nature == 1 else 'credit'] = abs(cha_tem.factor.factored_value(acc_con.accountable, acc_con.date, acc_con.value, cha_tem.nature))
            cha_dat['credit' if cha_tem.nature == 1 else 'debit'] = 0
            formset_data.append(cha_dat)
        formset = self.formset(request.POST, initial=formset_data)
        if not form.is_valid() or not formset.is_valid():
            form.set_readonly_fields(self.readonly_fields)
            context = {'form': form, 'formset':formset, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields':self.choice_fields, 'acc_pk':acc.pk, 'readonly_fields':self.readonly_fields}
            return render(request, self.template, context)
        form.creator = request.user
        ledger = form.save()            
        formset.creator = request.user
        formset.save(ledger)
        return redirect('accountables:lease_realty_accounting', acc_con.accountable.pk)
 
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
        formset = self.formset(initial=Accountable_Concept.pending.ledger_type_dict(typ_abr, capped=True))
        context = {'formset': formset, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields':self.choice_fields, 'hidden_fields':self.hidden_fields}
        return render(request, self.template, context)

    def post(self, request, typ_abr):
        formset = self.formset(request.POST, initial=Accountable_Concept.pending.ledger_type_dict(typ_abr, capped=True))
        if not formset.is_valid():
            context = {'formset': formset, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user), 'choice_fields':self.choice_fields}
            return render(request, self.template, context)
        formset.save(request.user)    
        return redirect('accountables:lease_realty_main')
 
 
class Ledger_TemplateRegisterReceiptView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'accounting/accountable_receipt.html'
    accountable_form = AccountableAccountingForm
    pending_charge_formset = ChargeReceivablePendingFormSet
    ledgerform = LedgerCreateModelForm
    chargeformset = ChargeCreate4AccountableFormset
    title = title
    subtitle = 'Crear Registro'
    ref_urls = ref_urls
    permission_required = 'accounting.add_ledger'
    readonly_fields = ['type', 'holder', 'third_party']
    choice_fields = ['type', 'holder', 'third_party']

    def get(self, request, ac_pk, typ_str):
        acc = Accountable.active.get(pk=ac_pk)
        accountable_form = self.accountable_form(instance=acc)
        pending_charge_formset = self.pending_charge_formset(initial=acc.subclass_obj().charge_receivable(ACCOUNT_RECEIPT_PRIORITY))
        ledger_form = self.ledgerform(initial={'type':Ledger_Type.objects.get(abreviation=typ_str), 'holder':acc.ledger_holder(), 'third_party':acc.ledger_third_party(), 'date':datetime.date.today()})
        ledger_form.set_readonly_fields(self.readonly_fields)
        chargeformset = self.chargeformset(acc)
        context = {'accountable_form': accountable_form, 'pending_charge_formset':pending_charge_formset, 'ledger_form':ledger_form, 'chargeformset':chargeformset, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user), 'choice_fields':self.choice_fields}
        return render(request, self.template, context)

    def post(self, request, ac_pk, typ_str):
        acc = Accountable.active.get(pk=ac_pk)
        ledger_form = self.ledgerform(request.POST, initial={'type':Ledger_Type.objects.get(abreviation=typ_str), 'holder':acc.ledger_holder(), 'third_party':acc.ledger_third_party(), 'date':datetime.date.today()})
        chargeformset = self.chargeformset(acc, request.POST)
        if not ledger_form.is_valid() or not chargeformset.is_valid():
            ledger_form.set_readonly_fields(self.readonly_fields)
            accountable_form = self.accountable_form(instance=acc)
            pending_charge_formset = self.pending_charge_formset(initial=acc.subclass_obj().charge_receivable(ACCOUNT_RECEIPT_PRIORITY))
            context = {'accountable_form': accountable_form, 'pending_charge_formset':pending_charge_formset, 'ledger_form':ledger_form, 'chargeformset':chargeformset, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user), 'choice_fields':self.choice_fields}
            return render(request, self.template, context)
        ledger_form.creator = request.user
        ledger = ledger_form.save()            
        chargeformset.creator = request.user
        chargeformset.save(ledger)
        return redirect('accountables:lease_realty_accounting', acc.pk)
