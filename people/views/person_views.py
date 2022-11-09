from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericListView, GenericDetailView,  GenericDeleteView, GenericActivateView
from people.models import Person, Person_Natural, Person_Legal
from people.forms.person_forms import PersonCreateForm, Person_NaturalCreateForm, Person_LegalCreateForm, Person_NaturalDetailForm, Person_LegalDetailForm, Person_NaturalUpdateForm, Person_LegalUpdateForm, Person_NaturalDeleteForm, Person_LegalDeleteForm, Person_NaturalActivateForm, Person_LegalActivateForm, PersonListModelFormSet
from people.utils import person_natural_related_data, person_legal_related_data, GetActionsOn, GetIncludedStates
from adin.utils.related_models import related_data_formsets_call

title = Person._meta.verbose_name_plural
ref_urls = { 'list':'people:person_list', 'create':'people:person_create', 'detail':'people:person_detail', 'update':'people:person_update', 'delete':'people:person_delete', 'activate': 'people:person_activate' }

class PersonListView(GenericListView):

    formset = PersonListModelFormSet
    model = Person
    choice_fields = ['id_type']
    title = title
    ref_urls = ref_urls
    actions_on = GetActionsOn
    list_order = 'complete_name'
    permission_required = 'people.view_person'
    include_states = GetIncludedStates

class PersonCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_create.html'
    form = PersonCreateForm
    title = title
    subtitle = 'Escoger tipo'
    ref_urls = ref_urls
    permission_required = 'people.add_person'

    def get(self, request):
        form = self.form()
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls}
        return render(request, self.template, context)

    def post(self, request):
        form = self.form(request.POST)
        if not form.is_valid():
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls}
            return render(request, self.template, context)
        if int(form['type'].value()) == 0:
            return redirect('people:person_natural_create')
        elif int(form['type'].value()) == 1:
            return redirect('people:person_legal_create')
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls}
        return render(request, self.template, context)

class Person_NaturalCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_create.html'
    form = Person_NaturalCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['type']
    choice_fields = ['type']
    permission_required = 'people.add_person'
    
    def get(self, request):
        form = self.form(initial={'type': 0})
        if self.readonly_fields:
            form.set_readonly_fields(self.readonly_fields)
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields': self.choice_fields}
        return render(request, self.template, context)

    def post(self, request):
        form = self.form(request.POST)
        if not form.is_valid():
            if self.readonly_fields:
                form.set_readonly_fields(self.readonly_fields)
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields': self.choice_fields}
            return render(request, self.template, context)
        form.creator = request.user
        per = form.save()            
        return redirect(self.ref_urls['update'], per.pk)

class Person_LegalCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_create.html'
    form = Person_LegalCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['type', 'id_type']
    choice_fields = ['type', 'id_type']
    permission_required = 'people.add_person'
    
    def get(self, request):
        form = self.form(initial={'type': 1, 'id_type': 1})
        if self.readonly_fields:
            form.set_readonly_fields(self.readonly_fields)
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields': self.choice_fields}
        return render(request, self.template, context)

    def post(self, request):
        form = self.form(request.POST)
        if not form.is_valid():
            if self.readonly_fields:
                form.set_readonly_fields(self.readonly_fields)
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields': self.choice_fields}
            return render(request, self.template, context)
        form.creator = request.user
        per = form.save()            
        return redirect(self.ref_urls['update'], per.pk)

class PersonDetailView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'people.view_person'

    def get(self, request, pk):
        per = Person.objects.get(pk=pk)
        if per.type == 0:
            return redirect('people:person_natural_detail', pk)
        elif per.type == 1:
            return redirect('people:person_legal_detail', pk)
        return redirect(self.ref_urls['list'])

class Person_NaturalDetailView(GenericDetailView):

    title = title
    model = Person_Natural
    form = Person_NaturalDetailForm
    ref_urls = ref_urls
    choice_fields = ['type', 'id_type', 'use']
    fk_fields = [ 'address' ]
    related_data = person_natural_related_data
    actions_on = GetActionsOn
    permission_required = 'people.view_person'

class Person_LegalDetailView(GenericDetailView):

    title = title
    model = Person_Legal
    form = Person_LegalDetailForm
    ref_urls = ref_urls
    choice_fields = ['type', 'id_type', 'use', 'appointment']
    fk_fields = [ 'address', 'person_natural' ]
    related_data = person_legal_related_data
    actions_on = GetActionsOn
    permission_required = 'people.view_person'

class PersonUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_update.html'
    form = {'Person_Natural':Person_NaturalUpdateForm, 'Person_Legal': Person_LegalUpdateForm}
    title = title
    subtitle = 'Actualizar'
    ref_urls = ref_urls
    readonly_fields = ['state', 'type', 'id_type', 'id_number']
    choice_fields = {'Person_Natural':['type', 'id_type', 'use'], 'Person_Legal': ['type', 'id_type', 'use', 'legal_type', 'appointment']}
    fk_fields = {'Person_Natural':[ 'address' ], 'Person_Legal': [ 'address', 'person_natural' ]}
    related_data = {'Person_Natural':person_natural_related_data, 'Person_Legal': person_legal_related_data}
    actions_on = GetActionsOn
    permission_required = 'people.change_person'

    def get(self, request, pk):
        obj = Person.objects.get(pk=pk)
        obj = obj.subclass_obj()
        model_str = obj._meta.model.__name__
        form = self.form[model_str](instance=obj)
        form.set_readonly_fields(self.readonly_fields)
        related_data = related_data_formsets_call(self.related_data[model_str], pk, request.user)
        actions_on = self.actions_on(request.user, model_str)
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields': self.choice_fields[model_str], 'fk_fields': self.fk_fields[model_str], 'related_data':related_data, 'actions_on': actions_on}
        return render(request, self.template, context)

    def post(self, request, pk):
        obj = Person.objects.get(pk=pk)
        obj = obj.subclass_obj()
        model_str = obj._meta.model.__name__
        form = self.form[model_str](request.POST, instance=obj)
        if not form.is_valid():
            related_data = related_data_formsets_call(self.related_data[model_str], pk, request.user)
            actions_on = self.actions_on(request.user, model_str)
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields': self.choice_fields[model_str], 'fk_fields': self.fk_fields[model_str], 'related_data':related_data, 'actions_on': actions_on}
            return render(request, self.template, context)
        form.save()
        return redirect(self.ref_urls['list'])

class PersonDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'people.delete_person'

    def get(self, request, pk):
        per = Person.objects.get(pk=pk)
        if per.type == 0:
            return redirect('people:person_natural_delete', pk)
        elif per.type == 1:
            return redirect('people:person_legal_delete', pk)
        return redirect(self.ref_urls['list'])

class Person_NaturalDeleteView(GenericDeleteView):

    title = title
    model = Person_Natural
    form = Person_NaturalDeleteForm
    ref_urls = ref_urls
    choice_fields = ['type', 'id_type', 'use']
    fk_fields = [ 'address' ]
    related_data = person_natural_related_data
    actions_on = GetActionsOn
    permission_required = 'people.delete_person'

class Person_LegalDeleteView(GenericDeleteView):

    title = title
    model = Person_Legal
    form = Person_LegalDeleteForm
    ref_urls = ref_urls
    choice_fields = ['type', 'id_type', 'use', 'appointment']
    fk_fields = [ 'address', 'person_natural' ]
    related_data = person_legal_related_data
    actions_on = GetActionsOn
    permission_required = 'people.delete_person'

class PersonActivateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'people.activate_person'

    def get(self, request, pk):
        per = Person.objects.get(pk=pk)
        if per.type == 0:
            return redirect('people:person_natural_activate', pk)
        elif per.type == 1:
            return redirect('people:person_legal_activate', pk)
        return redirect(self.ref_urls['list'])

class Person_NaturalActivateView(GenericActivateView):

    title = title
    model = Person_Natural
    form = Person_NaturalActivateForm
    ref_urls = ref_urls
    choice_fields = ['type', 'id_type', 'use']
    fk_fields = [ 'address' ]
    related_data = person_natural_related_data
    actions_on = GetActionsOn
    permission_required = 'people.activate_person'
    success_url = 'detail'

class Person_LegalActivateView(GenericActivateView):

    title = title
    model = Person_Legal
    form = Person_LegalActivateForm
    ref_urls = ref_urls
    choice_fields = ['type', 'id_type', 'use', 'appointment']
    fk_fields = [ 'address', 'person_natural' ]
    related_data = person_legal_related_data
    actions_on = GetActionsOn
    permission_required = 'people.activate_person'
    success_url = 'update'