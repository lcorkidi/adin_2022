from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from accountables.forms.lease_realty_transaction_type_forms import Lease_Realty_Transaction_TypeFrom
from accountables.models import Lease_Realty

title = 'Tipo de Cargo'
ref_urls = { 'list':'accountables:lease_realty_list', 'create':'accountables:lease_realty_create', 'detail':'accountables:lease_realty_detail', 'update':'accountables:lease_realty_update', 'delete':'accountables:lease_realty_delete', 'activate':'accountables:lease_realty_activate', 'accounting':'accountables:lease_realty_accounting' }
rel_urls = { 'add': 'accountables:lease_realty_transaction_type_add' }

class Lease_Realty_Transaction_TypeAddView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_m2m_add.html'
    model = Lease_Realty
    form = Lease_Realty_Transaction_TypeFrom
    title = title
    subtitle = 'Adicionar'
    ref_urls = ref_urls
    permission_required = 'accountables.accounting_lease_realty'

    def get(self, request, pk):
        obj = self.model.active.get(pk=pk)
        form = self.form(initial={'accountable':obj})
        context = { 'form': form, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'ref_pk': pk}
        return render(request, self.template, context)

    def post(self, request, pk):
        form = self.form(request.POST)
        if not form.is_valid():
            context = { 'form': form, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'ref_pk': pk}
            return render(request, self.template, context)
        form.add()
        return redirect(ref_urls['accounting'], pk)

class Lease_Realty_Transaction_TypeRemoveView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_m2m_remove.html'
    form = Lease_Realty_Transaction_TypeFrom
    title = title
    subtitle = 'Retirar'
    ref_urls = ref_urls
    rel_urls = rel_urls
    fk_fields = ['tranasction_type']
    permission_required = 'accountables.accounting_lease_realty'

    def get(self, request, pk):
        return render(request, self.template)
