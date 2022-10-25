from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView, GenericActivateView
from accounting.models import Ledger_Template
from accountables.models import Accountable, Accountable_Concept
from accounting.forms.ledger_template_forms import Ledger_TemplateDetailModelForm, Ledger_TemplateCreateModelForm, Ledger_TemplateDeleteModelForm, Ledger_TemplateSelectForm, Ledger_TemplateSelectAccountableForm, Ledger_TemplateConceptDataForm, Ledger_TemplateSelectConceptForm, Ledger_TemplateListModelFormSet
from accounting.forms.charge_template_forms import Charge_TemplateCreateFormset
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
        acc_con = Accountable_Concept.pending.charge(acc, lt).earliest('date')
        form = self.form(initial={'ledger_template':lt, 'accountable':acc, 'accountable_concept':acc_con})
        form.set_readonly_fields(self.readonly_fields)
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user), 'choice_fields':self.choice_fields}
        return render(request, self.template, context)

    def post(self, request, lt_pk, acc_pk):
        lt = Ledger_Template.active.get(pk=lt_pk)
        acc = Accountable.active.get(pk=acc_pk)
        acc_con = Accountable_Concept.pending.charge(acc, lt).earliest('date')
        form = self.form(request.POST, initial={'ledger_template':lt, 'accountable':acc, 'accountable_concept':acc_con})
        if not form.is_valid():
            form.set_readonly_fields(self.readonly_fields)
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user), 'choice_fields':self.choice_fields}
            return render(request, self.template, context)
        ledger = form.save(request.user)    
        return redirect('accounting:ledger_detail', ledger.pk)
