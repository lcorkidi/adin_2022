from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from accountables.forms.accountable_concept_forms import Accountable_ConceptCreateForm, Accountable_ConceptDeleteForm, Accountable_ConceptActivateForm
from accountables.models import Accountable, Accountable_Concept
from accountables.utils import accountables_ref_urls

title = Accountable_Concept._meta.verbose_name_plural
rel_urls = { 'create': 'accountables:accountable_charge_concept_create' }

class Accountable_ConceptCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_create_related.html'
    form = Accountable_ConceptCreateForm
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

class Accountable_ConceptDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_delete_related.html'
    form = Accountable_ConceptDeleteForm
    title = title
    subtitle = 'Borrar'
    rel_urls = rel_urls
    permission_required = 'accountables.accounting_accountable'

    def get(self, request, ret_pk, pk):
        obj = Accountable.active.get(pk=pk)
        form = self.form(obj)
        ref_urls = accountables_ref_urls[obj.subclass.model]
        context = { 'form': form, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls, 'rel_urls': self.rel_urls, 'ref_pk': ret_pk, 'accounting':True}
        return render(request, self.template, context)

class Accountable_ConceptActivateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    form = Accountable_ConceptActivateForm
    title = title
    rel_urls = rel_urls
    permission_required = 'accountables.accounting_accountable'
