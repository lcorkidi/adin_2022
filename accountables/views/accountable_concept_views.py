from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from accountables.models.accountable import Transaction_Type

from adin.utils.user_data import user_group_str
from accountables.forms.accountable_concept_forms import Accountable_ConceptCreateForm, Accountable_ConceptDeleteForm, Accountable_ConceptActivateForm, Accountable_ConceptCreateSelectTransaction_TypeForm, Accountable_ConceptPendingBulkCreateForm, Accountable_ConceptPendingFormSet, Accountable_ConceptPendingBulkFormSet
from accountables.models import Accountable, Accountable_Concept, Lease_Realty
from accountables.utils.views_data import accountables_ref_urls

title = Accountable_Concept._meta.verbose_name_plural
rel_urls = { 'create': 'accountables:accountable_concept_create' }

class Accountable_ConceptCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_create_related.html'
    form = Accountable_ConceptCreateForm
    title = title
    subtitle = 'Crear'
    readonly_fields = ['accountable']
    permission_required = 'accountables.accounting_accountable'

    def get(self, request, pk):
        obj = Accountable.active.get(pk=pk)
        form = self.form(obj, {'accountable': pk})
        form.set_readonly_fields(self.readonly_fields)
        ref_urls = accountables_ref_urls[obj.subclass.model]
        context = { 'form': form, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls, 'ref_pk': pk, 'accounting':True}
        return render(request, self.template, context)

    def post(self, request, pk):
        obj = Accountable.active.get(pk=pk)
        form = self.form(obj, request.POST)
        ref_urls = accountables_ref_urls[obj.subclass.model]
        form.accountable = obj
        if not form.is_valid():
            form.set_readonly_fields(self.readonly_fields)
            context = { 'form': form, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls, 'ref_pk': pk, 'accounting':True}
            return render(request, self.template, context)
        form.save(request.user)
        return redirect(ref_urls['accounting'], pk)

class Accountable_ConceptAccountableAllPendingCreateSelectTransaction_TypeView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_create_related.html'
    form = Accountable_ConceptCreateSelectTransaction_TypeForm
    title = title
    subtitle = 'Escoger Tipo de Transaccion'
    readonly_fields = ['accountable']
    permission_required = 'accountables.accounting_accountable'

    def get(self, request, pk):
        obj = Accountable.active.get(pk=pk)
        form = self.form(obj, {'accountable': pk})
        form.set_readonly_fields(self.readonly_fields)
        ref_urls = accountables_ref_urls[obj.subclass.model]
        context = { 'form': form, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls, 'ref_pk': pk, 'accounting':True}
        return render(request, self.template, context)

    def post(self, request, pk):
        obj = Accountable.active.get(pk=pk)
        form = self.form(obj, request.POST)
        if not form.is_valid():
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user)}
            return render(request, self.template, context)
        return redirect('accountables:pending_accountable_concept_create', pk, form['transaction_type'].value())

class Accountable_ConceptAccountableAllPendingCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'accountables/accountable_concept_accountable_all_pending_create.html'
    formset = Accountable_ConceptPendingFormSet
    title = title
    subtitle = 'Crear'
    permission_required = 'accountables.accounting_accountable'

    def get(self, request, pk, tra_typ):
        obj = Accountable.active.get(pk=pk)
        tt = Transaction_Type.objects.get(pk=tra_typ)
        formset = self.formset(initial=obj.subclass_obj().pending_concept_data_dict_list(tt))
        ref_urls = accountables_ref_urls[obj.subclass.model]
        context = { 'formset': formset, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls, 'ref_pk':pk}
        return render(request, self.template, context)

    def post(self, request, pk, tra_typ):
        obj = Accountable.active.get(pk=pk)
        tt = Transaction_Type.objects.get(pk=tra_typ)
        formset = self.formset(request.POST, initial=obj.subclass_obj().pending_concept_data_dict_list(tt))
        ref_urls = accountables_ref_urls[obj.subclass.model]
        if not formset.is_valid():
            context = { 'formset': formset, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls, 'ref_pk':pk}
            return render(request, self.template, context)
        formset.creator = request.user
        formset.save()
        return redirect(ref_urls['accounting'], pk)

class Accountable_ConceptBulkPendingCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'accountables/accountable_concept_bulk_pending_create.html'
    formset = Accountable_ConceptPendingBulkFormSet
    title = title
    subtitle = 'Crear'
    permission_required = 'accountables.accounting_accountable'

    def get(self, request):
        transaction_type = Transaction_Type.objects.get(name='Canon Mensual Arriendo Inmueble')
        formset = self.formset(initial=Lease_Realty.pending.bulk_concept_data_dict_list(transaction_type))
        ref_urls = accountables_ref_urls['lease_realty']
        context = { 'formset': formset, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls}
        return render(request, self.template, context)

    def post(self, request):
        transaction_type = Transaction_Type.objects.get(name='Canon Mensual Arriendo Inmueble')
        formset = self.formset(request.POST, initial=Lease_Realty.pending.bulk_concept_data_dict_list(transaction_type))
        ref_urls = accountables_ref_urls['lease_realty']
        if not formset.is_valid():
            context = { 'formset': formset, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls}
            return render(request, self.template, context)
        formset.creator = request.user
        formset.save()
        return redirect('accountables:lease_realty_main')

class Accountable_ConceptSinglePendingCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_create.html'
    form = Accountable_ConceptPendingBulkCreateForm
    title = title
    subtitle = 'Crear'
    permission_required = 'accountables.accounting_accountable'

    def get(self, request, cnt):
        transaction_type = Transaction_Type.objects.get(name='Canon Mensual Arriendo Inmueble')
        form = self.form(initial=Lease_Realty.pending.bulk_concept_data_dict_list(transaction_type)[cnt])
        ref_urls = accountables_ref_urls['lease_realty']
        context = { 'form': form, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls}
        return render(request, self.template, context)

    def post(self, request, cnt):
        transaction_type = Transaction_Type.objects.get(name='Canon Mensual Arriendo Inmueble')
        form = self.form(request.POST, initial=Lease_Realty.pending.bulk_concept_data_dict_list(transaction_type)[cnt])
        ref_urls = accountables_ref_urls['lease_realty']
        if not form.is_valid():
            context = { 'form': form, 'title': self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls}
            return render(request, self.template, context)
        form.save(request.user)
        return redirect('accountables:lease_realty_main')

class Accountable_ConceptDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_delete_related.html'
    model = Accountable_Concept
    title = title
    subtitle = 'Inactivar'
    form = Accountable_ConceptDeleteForm
    rel_urls = rel_urls
    fk_fields = ['accountable', 'transaction_type']
    omit_actions = ['update']
    accounting = True
    permission_required = 'accountables.accounting_accountable'

    def get(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':accountables_ref_urls[obj.accountable.subclass.model], 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'omit_actions': self.omit_actions, 'form':form, 'ref_pk': ret_pk, 'group': user_group_str(request.user), 'accounting': self.accounting}
        return render(request, self.template, context)

    def post(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        ref_urls = accountables_ref_urls[obj.accountable.subclass.model]
        if not form.is_valid():
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':ref_urls, 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'omit_actions': self.omit_actions, 'form':form, 'errors':True, 'ref_pk':ret_pk,  'group': user_group_str(request.user), 'accounting': self.accounting}
            return render(request, self.template, context)
        form.save(request.user)
        return redirect(ref_urls['accounting'], ret_pk)

class Accountable_ConceptActivateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    rel_urls = rel_urls
    template = 'adin/generic_activate_related.html'
    model = Accountable_Concept
    title = title
    subtitle = 'Activar'
    form = Accountable_ConceptActivateForm
    rel_urls = rel_urls
    fk_fields = ['accountable', 'transaction_type']
    accounting = True
    permission_required = 'accountables.accounting_accountable'

    def get(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':accountables_ref_urls[obj.accountable.subclass.model], 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'form':form, 'ref_pk': ret_pk, 'group': user_group_str(request.user), 'accounting': self.accounting}
        return render(request, self.template, context)

    def post(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        ref_urls = accountables_ref_urls[obj.accountable.subclass.model]
        if not form.is_valid():
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': ref_urls, 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'form':form, 'errors':True, 'ref_pk':ret_pk, 'group': user_group_str(request.user), 'accounting': self.accounting}
            return render(request, self.template, context)
        form.save(request.user)
        return redirect(ref_urls['accounting'], ret_pk)
