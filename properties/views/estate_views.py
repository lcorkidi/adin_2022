from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from properties.forms.estate_forms import EstateListModelFormSet
from properties.models import Estate

title = Estate._meta.verbose_name_plural
ref_urls = { 'list':'properties:estate_list', 'create':'properties:estate_create', 'detail':'properties:estate_detail', 'update':'properties:estate_update', 'delete':'properties:estate_delete' }

class EstatesListView(LoginRequiredMixin, View):

    template = 'adin/generic_list.html'
    formset = EstateListModelFormSet
    choice_fields = ['id_type']
    title = title
    ref_urls = ref_urls
    
    def get(self, request):
        formset = self.formset(queryset=Estate.objects.all().exclude(state=0).order_by('code'))
        context = {'formset': formset, 'choice_fields': self.choice_fields, 'title': self.title, 'ref_urls': self.ref_urls}
        return render(request, self.template, context)
