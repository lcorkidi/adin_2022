from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView, GenericActivateView
from accounting.models import Ledger_Template
from accounting.forms.ledger_template_forms import Ledger_TemplateDetailModelForm, Ledger_TemplateCreateModelForm, Ledger_TemplateDeleteModelForm, Ledger_TemplateListModelFormSet
from accounting.forms.charge_template_forms import Charge_TemplateCreateFormset
from accounting.utils import ledger_template_related_data
from home.utils import user_group_str

title = Ledger_Template._meta.verbose_name_plural
ref_urls = { 'list':'accounting:ledger_template_list', 'create':'accounting:ledger_template_create', 'detail':'accounting:ledger_template_detail', 'delete':'accounting:ledger_template_delete', 'activate':'accounting:ledger_template_activate' }

class Ledger_TemplateListView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'accounting.view_ledger_template'

    def get(self, request):
        if request.user.has_perm('accounting.activate_ledger'):
            return redirect('accounting:ledger_template_list_all')
        else: 
            return redirect('accounting:ledger_template_list_some')

class Ledger_TemplateListSomeView(GenericListView):

    formset = Ledger_TemplateListModelFormSet
    model = Ledger_Template
    title = title
    ref_urls = ref_urls
    fk_fields = ['transaction_type', 'ledger_type']
    actions_off = ['update']
    list_order = 'code'
    permission_required = 'accounting.view_ledger_template'

class Ledger_TemplateListAllView(GenericListView):

    formset = Ledger_TemplateListModelFormSet
    model = Ledger_Template
    title = title
    ref_urls = ref_urls
    fk_fields = ['transaction_type', 'ledger_type']
    actions_off = ['update']
    list_order = 'code'
    permission_required = 'accounting.activate_ledger_template'
    include_states = [ 0, 1, 2, 3 ]

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
        # form.creator = request.user
        # ledger = form.save()            
        # formset.creator = request.user
        # formset.save(ledger)
        return redirect(self.ref_urls['list'])

class Ledger_TemplateDetailView(GenericDetailView):

    title = title
    model = Ledger_Template
    form = Ledger_TemplateDetailModelForm
    ref_urls = ref_urls
    fk_fields = ['transaction_type', 'ledger_type']
    choice_fields = ['nature']
    actions_off = ['update']
    related_data = ledger_template_related_data
    permission_required = 'accounting.view_ledger_template'

class Ledger_TemplateDeleteView(GenericDeleteView):

    title = title
    model = Ledger_Template
    form = Ledger_TemplateDeleteModelForm
    ref_urls = ref_urls
    fk_fields = ['transaction_type', 'ledger_type']
    choice_fields = ['nature']
    actions_off = ['update']
    related_data = ledger_template_related_data
    permission_required = 'accounting.delete_ledger_template'

class Ledger_TemplateActivateView(GenericActivateView):

    title = title
    model = Ledger_Template
    form = Ledger_TemplateDeleteModelForm
    ref_urls = ref_urls
    fk_fields = ['transaction_type', 'ledger_type']
    choice_fields = ['nature']
    actions_off = ['update']
    related_data = ledger_template_related_data
    permission_required = 'accounting.activate_ledger_template'
