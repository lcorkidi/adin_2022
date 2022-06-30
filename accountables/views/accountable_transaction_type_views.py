from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericListView, GenericCreateView, GenericDetailView, GenericDeleteView, GenericActivateView
from accountables.forms.accountable_transaction_type_forms import Accountable_Transaction_TypeDetailModelForm, Accountable_Transaction_TypeCreateModelForm, Accountable_Transaction_TypeDeleteModelForm, Accountable_Transaction_TypeActivateModelForm, Accountable_Transaction_TypeAddForm, Accountable_Transaction_TypeRemoveForm, Accountable_Transaction_TypeListModelFormSet
from accountables.models import Accountable, Accountable_Transaction_Type
from accountables.utils import accountables_ref_urls

title = Accountable_Transaction_Type._meta.verbose_name_plural
ref_urls = { 'list':'accountables:accountable_transaction_type_list', 'create':'accountables:accountable_transaction_type_create', 'detail':'accountables:accountable_transaction_type_detail', 'delete':'accountables:accountable_transaction_type_delete', 'activate':'accountables:accountable_transaction_type_activate', 'add': 'accountables:accountable_transaction_type_add' }
        
class Accountable_Transaction_TypeListView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'accountables.view_transaction_type'

    def get(self, request):
        if request.user.has_perm('accountables.activate_transaction_type'):
            return redirect('accountables:accountable_transaction_type_list_all')
        else: 
            return redirect('accountables:accountable_transaction_type_list_some')

class Accountable_Transaction_TypeListSomeView(GenericListView):

    template = 'adin/generic_list.html'
    formset = Accountable_Transaction_TypeListModelFormSet
    model = Accountable_Transaction_Type
    title = title
    ref_urls = ref_urls
    actions_off = ['update', 'detail']
    list_order = 'accountable_transaction_type'
    permission_required = 'references.view_accountable_transaction_type'

class Accountable_Transaction_TypeListAllView(GenericListView):

    template = 'adin/generic_list.html'
    formset = Accountable_Transaction_TypeListModelFormSet
    model = Accountable_Transaction_Type
    title = title
    ref_urls = ref_urls
    actions_off = ['update', 'detail']
    list_order = 'name'
    permission_required = 'accountables.activate_accountable_transaction_type'
    include_states = [ 0, 1, 2, 3 ]

class Accountable_Transaction_TypeCreateView(GenericCreateView):

    form = Accountable_Transaction_TypeCreateModelForm
    title = title
    ref_urls = ref_urls
    permission_required = 'accountables.add_accountable_transaction_type'

class Accountable_Transaction_TypeDetailView(GenericDetailView):

    title = title
    model = Accountable_Transaction_Type
    form = Accountable_Transaction_TypeDetailModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'accountables.view_accountable_transaction_type'

class Accountable_Transaction_TypeDeleteView(GenericDeleteView):

    title = title
    model = Accountable_Transaction_Type
    form = Accountable_Transaction_TypeDeleteModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'accountables.delete_accountable_transaction_type'

class Accountable_Transaction_TypeActivateView(GenericActivateView):

    title = title
    model = Accountable_Transaction_Type
    form = Accountable_Transaction_TypeActivateModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'accountables.activate_accountable_transaction_type'
    success_url = 'list'

class Accountable_Transaction_TypeAddView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_m2m_add.html'
    form = Accountable_Transaction_TypeAddForm
    title = title
    subtitle = 'Adicionar'
    permission_required = 'accountables.accounting_accountable'

    def get(self, request, pk):
        obj = Accountable.active.get(pk=pk)
        form = self.form(initial={'accountable':obj})
        ref_urls = accountables_ref_urls[obj.subclass.model]
        context = { 'form': form, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls, 'ref_pk': pk}
        return render(request, self.template, context)

    def post(self, request, pk):
        obj = Accountable.active.get(pk=pk)
        form = self.form(request.POST)
        ref_urls = accountables_ref_urls[obj.subclass.model]
        if not form.is_valid():
            context = { 'form': form, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls, 'ref_pk': pk}
            return render(request, self.template, context)
        form.add()
        return redirect(ref_urls['accounting'], pk)

class Accountable_Transaction_TypeRemoveView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_m2m_remove.html'
    form = Accountable_Transaction_TypeRemoveForm
    title = title
    subtitle = 'Retirar'
    rel_urls = ref_urls
    fk_fields = ['tranasction_type']
    permission_required = 'accountables.accounting_accountable'

    def get(self, request, pk, rel_pk):
        obj = Accountable.active.get(pk=pk)
        form = self.form(initial={'accountable':obj, 'transaction_type': obj.transaction_types.get(pk=rel_pk)})
        ref_urls = accountables_ref_urls[obj.subclass.model]
        context = { 'form': form, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls, 'rel_urls': self.rel_urls, 'ref_pk': pk}
        return render(request, self.template, context)

    def post(self, request, pk, rel_pk):
        obj = Accountable.active.get(pk=pk)
        form = self.form(request.POST, initial={'accountable':obj, 'transaction_type': obj.transaction_types.get(pk=rel_pk)})
        ref_urls = accountables_ref_urls[obj.subclass.model]
        if not form.is_valid():
            context = { 'form': form, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls, 'rel_urls': self.rel_urls, 'ref_pk': pk}
            return render(request, self.template, context)
        form.remove()
        return redirect(ref_urls['accounting'], pk)
