from django.shortcuts import render
from django.views.generic import View
from people.models import Person
from .forms import PersonListModelFormSet

class PeopleListView(View):

    template = 'people/people_list.html'
    formset = PersonListModelFormSet
    choice_fields = ['id_type']
    
    def get(self, request):
        formset = self.formset(queryset=Person.objects.all().order_by('complete_name'))
        context = {'formset': formset, 'choice_fields': self.choice_fields}
        return render(request, self.template, context)
