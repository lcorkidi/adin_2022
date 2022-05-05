from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from accountables.forms.accountable_transaction_type_forms import Accountable_Transaction_TypeAddForm, Accountable_Transaction_TypeRemoveForm
from accountables.models import Accountable
from accountables.utils import accountables_ref_urls

title = 'Tipo de Cargo'
rel_urls = { 'add': 'accountables:accountable_transaction_type_add' }

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
    rel_urls = rel_urls
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
