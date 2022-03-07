from django.shortcuts import render
from django.views.generic import View
from people.models import Person
from .forms import PersonListModelFormSet

class PeopleListView(View):

    template = 'people/people_list.html'
    formset = PersonListModelFormSet
    choice_fields = ['id_type']
    title = Person._meta.verbose_name_plural
    ref_urls = {'list':'people:people_list', 'create':'people:people_create', 'detail':'people:people_detail', 'update':'people:people_update', 'delete':'people:people_delete'}
    
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

    def get(self, request, pk):
        return render(request, self.template)

class PeopleUpdateView(View):

    template = 'people/people_update.html'

    def get(self, request, pk):
        return render(request, self.template)

class PeopleDeleteView(View):

    template = 'people/people_delete.html'

    def get(self, request, pk):
        return render(request, self.template)
