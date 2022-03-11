from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from adin.core.views import GenericDetailView, GenericUpdateView, GenericDeleteView, GenericCreateRelatedView, GenericUpdateRelatedView, GenericDeleteRelatedView
from people.models import *
from .forms import PersonCreateForm, Person_NaturalCreateForm, Person_LegalCreateForm, Person_PhoneCreateForm, Person_EmailCreateForm, Person_AddressCreateForm, Person_Legal_Person_NaturalCreateForm, Person_NaturalDetailForm, Person_LegalDetailForm, Person_NaturalUpdateForm, Person_LegalUpdateForm, Person_PhoneUpdateForm, Person_EmailUpdateForm, Person_AddressUpdateForm, Person_Legal_Person_NaturalUpdateForm, Person_NaturalDeleteForm, Person_LegalDeleteForm, PersonListModelFormSet
from .utils import person_natural_m2m_data, person_legal_m2m_data 

title = Person._meta.verbose_name_plural
ref_urls = { 'list':'people:people_list', 'create':'people:people_create', 'detail':'people:people_detail', 'update':'people:people_update', 'delete':'people:people_delete' }
rel_urls = { 'create': 'people:people_staff_create', 'delete': 'people:people_address_delete', 'update': 'people:people_staff_update' }

class PersonListView(LoginRequiredMixin, View):

    template = 'adin/generic_list.html'
    formset = PersonListModelFormSet
    choice_fields = ['id_type']
    title = title
    ref_urls = ref_urls
    
    def get(self, request):
        formset = self.formset(queryset=Person.objects.all().exclude(state=0).order_by('complete_name'))
        context = {'formset': formset, 'choice_fields': self.choice_fields, 'title': self.title, 'ref_urls': self.ref_urls}
        return render(request, self.template, context)

class PersonDetailView(LoginRequiredMixin, View):

    def get(self, request, pk):
        per = Person.objects.get(pk=pk)
        if per.type == 0:
            return redirect('people:people_natural_detail', pk)
        elif per.type == 1:
            return redirect('people:people_legal_detail', pk)
        return redirect(self.ref_urls['list'])

class Person_NaturalDetailView(GenericDetailView):

    title = title
    model = Person_Natural
    form = Person_NaturalDetailForm
    ref_urls = ref_urls
    choice_fields = ['type', 'id_type', 'use']
    m2m_data = person_natural_m2m_data

class Person_LegalDetailView(GenericDetailView):

    title = title
    model = Person_Legal
    form = Person_LegalDetailForm
    ref_urls = ref_urls
    choice_fields = ['type', 'id_type', 'use', 'appointment']
    m2m_data = person_legal_m2m_data

class PersonCreateView(LoginRequiredMixin, View):

    template = 'adin/generic_create.html'
    form = PersonCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    
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
            return redirect('people:people_natural_create')
        elif int(form['type'].value()) == 1:
            return redirect('people:people_legal_create')
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls}
        return render(request, self.template, context)

class Person_NaturalCreateView(LoginRequiredMixin, View):

    template = 'adin/generic_create.html'
    form = Person_NaturalCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['type']
    choice_fields = ['type']
    
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

class Person_LegalCreateView(LoginRequiredMixin, View):

    template = 'adin/generic_create.html'
    form = Person_LegalCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['type', 'id_type']
    choice_fields = ['type', 'id_type']
    
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

class Person_PhoneCreateView(GenericCreateRelatedView):

    template = 'people/people_related_create.html'
    form = Person_PhoneCreateForm
    title = Person_Phone._meta.verbose_name_plural
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['person']

class Peorson_EmailCreateView(GenericCreateRelatedView):

    template = 'people/people_related_create.html'
    form = Person_EmailCreateForm
    title = Person_E_Mail._meta.verbose_name_plural
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['person']

class Person_AddressCreateView(GenericCreateRelatedView):

    template = 'people/people_related_create.html'
    form = Person_AddressCreateForm
    title = Person_Address._meta.verbose_name_plural
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['person']

class Person_Legal_Person_NaturalCreateView(GenericCreateRelatedView):

    template = 'people/people_related_create.html'
    form = Person_Legal_Person_NaturalCreateForm
    title = Person_Legal_Person_Natural._meta.verbose_name_plural
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['person']

class PersonUpdateView(LoginRequiredMixin, View):

    def get(self, request, pk):
        per = Person.objects.get(pk=pk)
        if per.type == 0:
            return redirect('people:people_natural_update', pk)
        elif per.type == 1:
            return redirect('people:people_legal_update', pk)
        return redirect(self.ref_urls['list'])

class Person_NaturalUpdateView(GenericUpdateView):

    model = Person_Natural
    form = Person_NaturalUpdateForm
    title = title
    ref_urls = ref_urls
    readonly_fields = ['type', 'id_type', 'id_number']
    choice_fields = ['type', 'id_type', 'use']
    m2m_data = person_natural_m2m_data

class Person_LegalUpdateView(GenericUpdateView):

    model = Person_Legal
    form = Person_LegalUpdateForm
    title = title
    ref_urls = ref_urls
    readonly_fields = ['type', 'id_type', 'id_number']
    choice_fields = ['type', 'id_type', 'use', 'legal_type', 'appointment']
    m2m_data = person_legal_m2m_data

class Person_PhoneUpdateView(GenericUpdateRelatedView):

    template = 'people/people_related_update.html'
    model = Person_Phone
    form = Person_PhoneUpdateForm
    title = Person_Phone._meta.verbose_name_plural
    ref_urls = ref_urls
    rel_urls = { 'create': 'people:people_phone_create', 'delete': 'people:people_phone_delete'}
    readonly_fields = ['person', 'phone']

class Person_EmailUpdateView(GenericUpdateRelatedView):

    template = 'people/people_related_update.html'
    model = Person_E_Mail
    form = Person_EmailUpdateForm
    title = Person_E_Mail._meta.verbose_name_plural
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['person', 'email']

class Person_AddressUpdateView(GenericUpdateRelatedView):

    template = 'people/people_related_update.html'
    model = Person_Address
    form = Person_AddressUpdateForm
    title = Person_Address._meta.verbose_name_plural
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['person', 'address']

class Person_Legal_Person_NaturalUpdateView(GenericUpdateRelatedView):

    template = 'people/people_related_update.html'
    model = Person_Legal_Person_Natural
    form = Person_Legal_Person_NaturalUpdateForm
    title = Person_Legal_Person_Natural._meta.verbose_name_plural
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['person_legal', 'person_naural']

class PersonDeleteView(LoginRequiredMixin, View):

    def get(self, request, pk):
        per = Person.objects.get(pk=pk)
        if per.type == 0:
            return redirect('people:people_natural_delete', pk)
        elif per.type == 1:
            return redirect('people:people_legal_delete', pk)
        return redirect(self.ref_urls['list'])

class Person_NaturalDeleteView(GenericDeleteView):

    title = title
    model = Person_Natural
    form = Person_NaturalDeleteForm
    ref_urls = ref_urls
    choice_fields = ['type', 'id_type', 'use']
    m2m_data = person_natural_m2m_data

class Person_LegalDeleteView(GenericDeleteView):

    title = title
    model = Person_Legal
    form = Person_LegalDeleteForm
    ref_urls = ref_urls
    choice_fields = ['type', 'id_type', 'use', 'appointment']
    m2m_data = person_legal_m2m_data

class Person_PhoneDeleteView(GenericDeleteRelatedView):

    template = 'people/people_related_delete.html'
    model = Person_Phone
    form = Person_PhoneUpdateForm
    title = Person_Phone._meta.verbose_name_plural
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['use']

class Person_EmailDeleteView(GenericDeleteRelatedView):

    template = 'people/people_related_delete.html'
    model = Person_E_Mail
    form = Person_EmailUpdateForm
    title = Person_E_Mail._meta.verbose_name_plural
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['use']

class Person_AddressDeleteView(GenericDeleteRelatedView):

    template = 'people/people_related_delete.html'
    model = Person_Address
    form = Person_AddressUpdateForm
    title = Person_Address._meta.verbose_name_plural
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['use']

class Person_Legal_Person_NaturalDeleteView(GenericDeleteRelatedView):

    template = 'people/people_related_delete.html'
    model = Person_Legal_Person_Natural
    form = Person_Legal_Person_NaturalUpdateForm
    title = Person_Legal_Person_Natural._meta.verbose_name_plural
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['appointment']
