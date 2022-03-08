from django.shortcuts import redirect, render
from django.views.generic import View

from people.models import Person, Person_Natural, Person_Legal, Person_Phone, Person_Email, Person_Address
from .forms import PersonCreateForm, Person_NaturalCreateForm, Person_LegalCreateForm, PersonNaturalUpdateForm, PersonLegalUpdateForm, PersonListModelFormSet, Person_PhoneModelFormSet, Person_EmailModelFormSet, Person_AddressModelFormSet

per_title = Person._meta.verbose_name_plural
per_urls = { 'list':'people:people_list', 'create':'people:people_create', 'detail':'people:people_detail', 'update':'people:people_update', 'delete':'people:people_delete' }

class PeopleListView(View):

    template = 'people/people_list.html'
    formset = PersonListModelFormSet
    choice_fields = ['id_type']
    title = per_title
    ref_urls = per_urls
    
    def get(self, request):
        formset = self.formset(queryset=Person.objects.all().order_by('complete_name'))
        context = {'formset': formset, 'choice_fields': self.choice_fields, 'title': self.title, 'ref_urls': self.ref_urls}
        return render(request, self.template, context)

class PeopleDetailView(View):

    template = 'people/people_detail.html'

    def get(self, request, pk):
        return render(request, self.template)

class PeopleCreateView(View):

    template = 'people/people_create.html'
    form = PersonCreateForm
    title = per_title
    subtitle = 'Crear'
    ref_urls = per_urls
    
    def get(self, request):
        form = self.form()
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls}
        return render(request, self.template, context)

    def post(self, request):
        form = self.form(request.POST)
        if not form.is_valid():
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls}
            return render(request, self.template, context)
        print(type(form['type'].value()))
        if int(form['type'].value()) == 0:
            return redirect('people:people_natural_create')
        elif int(form['type'].value()) == 1:
            return redirect('people:people_legal_create')
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls}
        return render(request, self.template, context)

class People_NaturalCreateView(View):

    template = 'people/people_create.html'
    form = Person_NaturalCreateForm
    title = per_title
    subtitle = 'Crear'
    ref_urls = per_urls
    readonly_fields = ['type']
    choice_fields = ['type']
    
    def get(self, request):
        form = self.form(initial={'type': 0})
        if self.readonly_fields:
            form.set_readonly_fields(self.readonly_fields)
        form
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields': self.choice_fields}
        return render(request, self.template, context)

    def post(self, request):
        form = self.form(request.POST)
        if not form.is_valid():
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields': self.choice_fields}
            return render(request, self.template, context)
        form.creator = request.user
        form.save()            
        return redirect(self.ref_urls['list'])

class People_LegalCreateView(View):

    template = 'people/people_create.html'
    form = Person_LegalCreateForm
    title = per_title
    subtitle = 'Crear'
    ref_urls = per_urls
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
            context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields': self.choice_fields}
            return render(request, self.template, context)
        form.creator = request.user
        form.save()            
        return redirect(self.ref_urls['list'])

class People_PhoneCreateView(View):

    template = 'people/people_realted_create.html'

    def get(self, request, pk):
        return render(request, self.template)

class People_EmailCreateView(View):

    template = 'people/people_realted_create.html'

    def get(self, request, pk):
        return render(request, self.template)

class People_AddressCreateView(View):

    template = 'people/people_realted_create.html'

    def get(self, request, pk):
        return render(request, self.template)

class PeopleUpdateView(View):

    def get(self, request, pk):
        per = Person.objects.get(pk=pk)
        if per.type == 0:
            return redirect('people:people_natural_update', pk)
        elif per.type == 1:
            return redirect('people:people_legal_update', pk)
        return redirect(self.ref_urls['list'])

class People_NaturalUpdateView(View):

    template = 'people/people_update.html'
    form = PersonNaturalUpdateForm
    title = per_title
    subtitle = 'Actualizar'
    ref_urls = per_urls
    readonly_fields = ['type', 'id_type', 'id_number']
    choice_fields = ['type', 'id_type', 'use']

    def get(self, request, pk):
        per = Person_Natural.objects.get(pk=pk)
        form = self.form(instance=per)
        m2m_data = {
            'phone': {
                'class': Person_Phone,
                'formset': Person_PhoneModelFormSet,
                'create_url': 'people:people_phone_create',
                'update_url': 'people:people_phone_update',
                'delete_url': 'people:people_phone_delete'
            },
            'email': {
                'class': Person_Email,
                'formset': Person_EmailModelFormSet,
                'create_url': 'people:people_email_create',
                'update_url': 'people:people_email_update',
                'delete_url': 'people:people_email_delete'
            },
            'address': {
                'class': Person_Address,
                'formset': Person_AddressModelFormSet,
                'create_url': 'people:people_address_create',
                'update_url': 'people:people_address_update',
                'delete_url': 'people:people_address_delete'
            }        
        }
        if self.readonly_fields:
            form.set_readonly_fields(self.readonly_fields)
        for attr, data in m2m_data.items():
            formset = data['formset'](queryset=data['class'].objects.filter(person__id_number=pk))
            m2m_data[attr]['formset'] = formset
        context = {'form': form, 'title': self.title, 'subtitle': self.subtitle, 'ref_urls': self.ref_urls, 'choice_fields': self.choice_fields, 'm2m_data': m2m_data}
        return render(request, self.template, context)

class People_LegalUpdateView(View):

    template = 'people/people_detail.html'

    def get(self, request, pk):
        return render(request, self.template)

class People_PhoneUpdateView(View):

    template = 'people/people_realted_update.html'

    def get(self, request, pk):
        return render(request, self.template)

class People_EmailUpdateView(View):

    template = 'people/people_realted_update.html'

    def get(self, request, pk):
        return render(request, self.template)

class People_AddressUpdateView(View):

    template = 'people/people_realted_update.html'

    def get(self, request, pk):
        return render(request, self.template)

class PeopleDeleteView(View):

    template = 'people/people_delete.html'

    def get(self, request, pk):
        return render(request, self.template)

class People_PhoneDeleteView(View):

    template = 'people/people_realted_delete.html'

    def get(self, request, pk):
        return render(request, self.template)

class People_EmailDeleteView(View):

    template = 'people/people_realted_delete.html'

    def get(self, request, pk):
        return render(request, self.template)

class People_AddressDeleteView(View):

    template = 'people/people_realted_delete.html'

    def get(self, request, pk):
        return render(request, self.template)
