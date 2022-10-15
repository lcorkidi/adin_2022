from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from scripts.utils import model_load, models_info
from adin.utils.user_data import user_group_str
from adin.utils.related_models import related_data_formsets_call

class GenericListView(LoginRequiredMixin, PermissionRequiredMixin, View):
    
    template = 'adin/generic_list.html'
    formset = None
    model = None
    title = None
    ref_urls = None
    choice_fields = None
    fk_fields = None
    actions_on = None
    list_order = None
    include_states = None
    
    def get(self, request):
        include_states = self.include_states(request.user, self.model.__name__)
        actions_on = self.actions_on(request.user, self.model.__name__)
        formset = self.formset(queryset=self.model.objects.all().filter(state__in=include_states).order_by(self.list_order))
        context = {'formset': formset, 'title': self.title, 'ref_urls': self.ref_urls, 'choice_fields': self.choice_fields, 'fk_fields': self.fk_fields, 'actions_on': actions_on}
        return render(request, self.template, context)

class GenericCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_create.html'
    form = None
    title = None
    subtitle = 'Crear'
    ref_urls = None
    
    def get(self, request):
        form = self.form()
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request):
        form = self.form(request.POST)
        if not form.is_valid():
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user)}
            return render(request, self.template, context)
        form.creator = request.user
        form.save()            
        return redirect(self.ref_urls['list'])

class GenericDetailView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_detail.html'
    title = None
    subtitle = 'Ver'
    model = None
    form = None
    ref_urls = None
    choice_fields = None
    fk_fields = None
    related_data = None
    actions_off = None

    def get(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        related_data = related_data_formsets_call(self.related_data, pk)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'form':form, 'related_data':related_data, 'choice_fields':self.choice_fields, 'fk_fields': self.fk_fields, 'actions_off': self.actions_off, 'group': user_group_str(request.user) }
        return render(request, self.template, context)

class GenericUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_update.html'
    model = None
    form = None
    title = None
    subtitle = 'Actualizar'
    ref_urls = None
    readonly_fields = None
    choice_fields = None
    fk_fields = None
    related_data = None
    include_states = [ 1, 2, 3 ]

    def get(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        if self.readonly_fields:
            form.set_readonly_fields(self.readonly_fields)
        related_data = related_data_formsets_call(self.related_data, pk)
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields': self.choice_fields, 'fk_fields': self.fk_fields, 'related_data':related_data, 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        if self.readonly_fields:
            form.set_readonly_fields(self.readonly_fields)
        if not form.is_valid():
            related_data = related_data_formsets_call(self.related_data, pk)
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields': self.choice_fields, 'fk_fields': self.fk_fields, 'related_data':related_data, 'group': user_group_str(request.user)}
            return render(request, self.template, context)
        form.save()
        return redirect(self.ref_urls['list'])

class GenericDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_delete.html'
    title = None
    subtitle = 'Inactivar'
    model = None
    form = None
    ref_urls = None
    choice_fields = None
    fk_fields = None
    related_data = None
    actions_off = None

    def get(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        related_data = related_data_formsets_call(self.related_data, pk)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'form':form, 'related_data':related_data, 'choice_fields':self.choice_fields, 'fk_fields': self.fk_fields, 'actions_off': self.actions_off , 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        related_data = related_data_formsets_call(self.related_data, pk)
        if not form.is_valid():
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'form':form, 'related_data':related_data, 'choice_fields':self.choice_fields, 'fk_fields': self.fk_fields, 'actions_off': self.actions_off , 'group': user_group_str(request.user)}
            return render(request, self.template, context)
        if related_data:    
            for key, data in related_data.items():
                for form in data['formset']:
                    ins = form.instance
                    ins.state = 0
                    ins.save()
        obj.state = 0
        obj.save()
        return redirect(self.ref_urls['list'])

class GenericActivateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_activate.html'
    title = None
    subtitle = 'Activar'
    model = None
    form = None
    ref_urls = None
    choice_fields = None
    fk_fields = None
    related_data = None
    actions_off = None
    success_url = 'update'

    def get(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        related_data = related_data_formsets_call(self.related_data, pk)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'form':form, 'related_data':related_data, 'choice_fields':self.choice_fields, 'fk_fields': self.fk_fields, 'actions_off': self.actions_off , 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        if not form.is_valid():
            related_data = related_data_formsets_call(self.related_data, pk)
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'form':form, 'related_data':related_data, 'choice_fields':self.choice_fields, 'fk_fields': self.fk_fields, 'actions_off': self.actions_off , 'group': user_group_str(request.user)}
            return render(request, self.template, context)
        obj.state = 2
        obj.save()
        if self.success_url != 'list':
            return redirect(self.ref_urls[self.success_url], obj.pk)
        else:
            return redirect(self.ref_urls[self.success_url])

class GenericCreateRelatedView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_create_related.html'
    form = None
    title = None
    subtitle = 'Crear'
    ref_urls = None
    readonly_fields = None
    fk_fields = None
    related_fields = None

    def get(self, request, pk):
        form = self.form({self.readonly_fields[0]:pk})
        form.set_readonly_fields(self.readonly_fields)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'fk_fields': self.fk_fields, 'form':form, 'errors':False, 'ref_pk':pk, 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request, pk):
        form = self.form(request.POST)
        form.related_fields = self.related_fields
        if not form.is_valid():
            form.set_readonly_fields(self.readonly_fields)
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'fk_fields': self.fk_fields, 'form':form, 'errors':True, 'ref_pk':pk, 'group': user_group_str(request.user)}
            return render(request, self.template, context)
        form.creator = request.user
        form.save()            
        return redirect(self.ref_urls['update'], pk)

class GenericDetailRelatedlView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_detail_related.html'
    model = None
    title = None
    subtitle = 'Inactivar'
    form = None
    ref_urls = None
    rel_urls = None
    choice_fields = None
    fk_fields = None
    omit_actions = None

    def get(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'omit_actions': self.omit_actions, 'form':form, 'ref_pk': ret_pk, 'choice_fields':self.choice_fields, 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        if not form.is_valid():
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'omit_actions': self.omit_actions, 'form':form, 'errors':True, 'ref_pk':ret_pk,'choice_fields':self.choice_fields,  'group': user_group_str(request.user)}
            return render(request, self.template, context)
        obj.state_change_user = request.user
        obj.state = 0
        obj.save()
        return redirect(self.ref_urls['update'], ret_pk)

class GenericUpdateRelatedView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_update_related.html'
    model = None
    form = None
    title = None
    subtitle = 'Actualizar'
    ref_urls = None
    rel_urls = None
    readonly_fields = None
    fk_fields = None

    def get(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        form.set_readonly_fields(self.readonly_fields)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'form':form, 'errors':False, 'ref_pk':ret_pk, 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        if not form.is_valid():
            form.set_readonly_fields(self.readonly_fields)
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'form':form, 'errors':True, 'ref_pk':ret_pk, 'group': user_group_str(request.user)}
            return render(request, self.template, context)
        form.creator = request.user
        form.save(self.readonly_fields)           
        return redirect(self.ref_urls['update'], ret_pk)

class GenericDeleteRelatedView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_delete_related.html'
    model = None
    title = None
    subtitle = 'Inactivar'
    form = None
    ref_urls = None
    rel_urls = None
    choice_fields = None
    fk_fields = None
    omit_actions = None
    accounting = False

    def get(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'omit_actions': self.omit_actions, 'form':form, 'ref_pk': ret_pk, 'choice_fields':self.choice_fields, 'group': user_group_str(request.user), 'accounting': self.accounting}
        return render(request, self.template, context)

    def post(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        if not form.is_valid():
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'omit_actions': self.omit_actions, 'form':form, 'errors':True, 'ref_pk':ret_pk,'choice_fields':self.choice_fields,  'group': user_group_str(request.user), 'accounting': self.accounting}
            return render(request, self.template, context)
        obj.state_change_user = request.user
        obj.state = 0
        obj.save()
        return redirect(self.ref_urls['update'], ret_pk)

class GenericActivateRelatedView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_activate_related.html'
    model = None
    title = None
    subtitle = 'Activar'
    form = None
    ref_urls = None
    rel_urls = None
    choice_fields = None
    fk_fields = None
    accounting = False
    
    def get(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'form':form, 'ref_pk': ret_pk, 'choice_fields':self.choice_fields, 'group': user_group_str(request.user), 'accounting': self.accounting}
        return render(request, self.template, context)

    def post(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        if not form.is_valid():
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'form':form, 'errors':True, 'ref_pk':ret_pk, 'group': user_group_str(request.user), 'accounting': self.accounting}
            return render(request, self.template, context)
        obj.state = 2
        obj.save()
        return redirect(self.ref_urls['update'], ret_pk)

class GenericCreateBulkView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_create_bulk.html'
    title = None
    subtitle = 'Crear'
    ref_urls = None
    
    def get(self, request):
        context = {'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request):
        model_load(models_info['puc'], request.FILES['csv'])
        return redirect(self.ref_urls['list'])

class GenericDeleteBulkView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_delete_bulk.html'
    title = None
    subtitle = 'Borrar'
    model = None
    ref_urls = None
    
    def get(self, request):
        context = {'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request):
        self.model.objects.all().delete()
        return redirect(self.ref_urls['list'])

