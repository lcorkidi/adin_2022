from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from accountables.forms.accountable_charge_concept_forms import Accountable_Charge_ConceptCreateForm, Accountable_Charge_ConceptDeleteForm, Accountable_Charge_ConceptActivateForm
from accountables.models import Accountable
from accountables.utils import accountables_ref_urls

title = 'Concepto Cargo'
rel_urls = { 'create': 'accountables:lease_realty_person_create', 'delete': 'accountables:lease_realty_person_delete', 'update': 'accountables:lease_realty_person_update' }

class Accountable_Charge_ConceptCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_create_related.html'
    form = Accountable_Charge_ConceptCreateForm
    title = title
    subtitle = 'Crear'
    permission_required = 'accountables.accounting_accountable'

    def get(self, request, pk):
        obj = Accountable.active.get(pk=pk)
        form = self.form(obj)
        ref_urls = accountables_ref_urls[obj.subclass.model]
        context = { 'form': form, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls, 'ref_pk': pk, 'accounting':True}
        return render(request, self.template, context)

    def post(self, request, pk):
        obj = Accountable.active.get(pk=pk)
        form = self.form(obj, request.POST)
        ref_urls = accountables_ref_urls[obj.subclass.model]
        form.accountable = obj
        if not form.is_valid():
            context = { 'form': form, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls, 'ref_pk': pk, 'accounting':True}
            return render(request, self.template, context)
        form.creator = request.user
        form.save()
        return redirect(ref_urls['accounting'], pk)

class Accountable_Charge_ConceptDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):

    form = Accountable_Charge_ConceptDeleteForm
    title = title
    rel_urls = rel_urls
    permission_required = 'accountables.accounting_accountable'

class Accountable_Charge_ConceptActivateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    form = Accountable_Charge_ConceptActivateForm
    title = title
    rel_urls = rel_urls
    permission_required = 'accountables.accounting_accountable'
