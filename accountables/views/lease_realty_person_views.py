from django.shortcuts import render, redirect
from adin.core.views import GenericCreateRelatedView, GenericUpdateRelatedView, GenericDeleteRelatedView, GenericActivateRelatedView

from accountables.models import Lease_Realty_Person
from accountables.forms.lease_realty_person_forms import Lease_Realty_PersonCreateForm, Lease_Realty_PersonUpdateForm, Lease_Realty_PersonDeleteForm, Lease_Realty_PersonActivateForm
from home.utils import user_group_str

title = Lease_Realty_Person._meta.verbose_name_plural
ref_urls = { 'list':'accountables:lease_realty_list', 'create':'accountables:lease_realty_create', 'detail':'accountables:lease_realty_detail', 'update':'accountables:lease_realty_update', 'delete':'accountables:lease_realty_delete' }
rel_urls = { 'create': 'accountables:lease_realty_person_create', 'delete': 'accountables:lease_realty_person_delete', 'update': 'accountables:lease_realty_person_update' }

class Lease_Realty_PersonCreateView(GenericCreateRelatedView):

    form = Lease_Realty_PersonCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['lease']
    fk_fields = ['lease']
    permission_required = 'accountables.add_lease_realty_person'
    related_fields = ['lease', 'person']

class Lease_Realty_PersonUpdateView(GenericUpdateRelatedView):

    model = Lease_Realty_Person
    form = Lease_Realty_PersonUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['lease', 'person']
    fk_fields = ['lease', 'person']
    permission_required = 'accountables.change_lease_realty_person'

class Lease_Realty_PersonDeleteView(GenericDeleteRelatedView):

    template = 'adin/generic_delete_related.html'
    subtitle = 'Inactivar'
    model = Lease_Realty_Person
    form = Lease_Realty_PersonDeleteForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['role']
    fk_fields = ['lease', 'person']
    permission_required = 'accountables.delete_lease_realty_person'

    def get(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        base_args = dict((key[:len(key)-3] if key.endswith('_id') else key, value) for key, value in obj.__dict__.items() if not callable(value) and not key.startswith('_') and not key.startswith('id') and not key.startswith('state'))
        form = self.form(initial=base_args)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'omit_actions': self.omit_actions, 'form':form, 'ref_pk': ret_pk, 'choice_fields':self.choice_fields, 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        base_args = dict((key[:len(key)-3] if key.endswith('_id') else key, value) for key, value in obj.__dict__.items() if not callable(value) and not key.startswith('_') and not key.startswith('id') and not key.startswith('state'))
        form = self.form(request.POST, initial=base_args)
        if not form.is_valid():
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'omit_actions': self.omit_actions, 'form':form, 'errors':True, 'ref_pk':ret_pk,'choice_fields':self.choice_fields,  'group': user_group_str(request.user)}
            return render(request, self.template, context)
        obj.state_change_user = request.user
        obj.state = 0
        obj.save()
        return redirect(self.ref_urls['update'], ret_pk)

class Lease_Realty_PersonActivateView(GenericActivateRelatedView):

    template = 'adin/generic_activate_related.html'
    subtitle = 'Activar'
    model = Lease_Realty_Person
    form = Lease_Realty_PersonActivateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['role']
    fk_fields = ['lease', 'person']
    permission_required = 'accountables.activate_lease_realty'
    
    def get(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        base_args = dict((key[:len(key)-3] if key.endswith('_id') else key, value) for key, value in obj.__dict__.items() if not callable(value) and not key.startswith('_') and not key.startswith('id') and not key.startswith('state'))
        form = self.form(initial=base_args)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'form':form, 'ref_pk': ret_pk, 'choice_fields':self.choice_fields, 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        base_args = dict((key[:len(key)-3] if key.endswith('_id') else key, value) for key, value in obj.__dict__.items() if not callable(value) and not key.startswith('_') and not key.startswith('id') and not key.startswith('state'))
        form = self.form(request.POST, initial=base_args)
        if not form.is_valid():
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'form':form, 'errors':True, 'ref_pk':ret_pk, 'group': user_group_str(request.user)}
            return render(request, self.template, context)
        obj.state = 2
        obj.save()
        return redirect(self.ref_urls['update'], ret_pk)
