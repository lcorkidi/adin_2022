from traceback import format_exc
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericDeleteRelatedView
from accountables.forms.accountable_concept_forms import Accountable_ConceptCreateForm, Accountable_ConceptDeleteForm, Accountable_ConceptActivateForm, Accountable_ConceptPendingFormSet
from accountables.models import Accountable, Accountable_Concept
from accountables.utils import accountables_ref_urls

title = Accountable_Concept._meta.verbose_name_plural
rel_urls = { 'create': 'accountables:accountable_concept_create' }

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

class Accountable_ConceptPendingCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'accountables/accountable_concept_pending_create.html'
    formset = Accountable_ConceptPendingFormSet
    title = title
    subtitle = 'Crear'
    permission_required = 'accountables.accounting_accountable'

    def get(self, request, pk):
        obj = Accountable.active.get(pk=pk)
        formset = self.formset(initial=obj.subclass_obj().concept_formset_dict(), form_kwargs={'accountable':obj})
        ref_urls = accountables_ref_urls[obj.subclass.model]
        context = { 'formset': formset, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls}
        return render(request, self.template, context)

    def post(self, request, pk):
        obj = Accountable.active.get(pk=pk)
        formset = self.formset(request.POST, initial=obj.subclass_obj().concept_formset_dict(), form_kwargs={'accountable':obj})
        ref_urls = accountables_ref_urls[obj.subclass.model]
        ref_urls = accountables_ref_urls[obj.subclass.model]
        if not formset.is_valid():
            context = { 'formset': formset, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls}
            return render(request, self.template, context)
        formset.creator = request.user
        formset.save()
        return redirect(ref_urls['accounting'], pk)

class Accountable_ConceptDeleteView(GenericDeleteRelatedView):

    template = 'adin/generic_delete_related.html'
    model = Accountable_Concept
    title = title
    subtitle = 'Inactivar'
    form = Accountable_ConceptDeleteForm
    rel_urls = rel_urls
    fk_fields = ['accountable', 'transaction_type']
    omit_actions = ['update']
    permission_required = 'accountables.accounting_accountable'

    def get(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':accountables_ref_urls[obj.subclass.model], 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'omit_actions': self.omit_actions, 'form':form, 'ref_pk': ret_pk, 'choice_fields':self.choice_fields, 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        ref_urls = accountables_ref_urls[obj.subclass.model]
        if not form.is_valid():
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':ref_urls, 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'omit_actions': self.omit_actions, 'form':form, 'errors':True, 'ref_pk':ret_pk,'choice_fields':self.choice_fields,  'group': user_group_str(request.user)}
            return render(request, self.template, context)
        form.save(kwargs={'user': request.user, 'state':0})
        return redirect(ref_urls['update'], ret_pk)

class Accountable_ConceptActivateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    form = Accountable_ConceptActivateForm
    title = title
    rel_urls = rel_urls
    permission_required = 'accountables.accounting_accountable'
