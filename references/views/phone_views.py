from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from adin.core.views import GenericDetailView, GenericCreateView, GenericDeleteView
from references.models import Phone
from references.forms.phone_forms import PhoneDetailModelForm, PhoneCreateModelForm, PhoneDeleteModelForm, PhoneListModelFormSet

title = Phone._meta.verbose_name_plural
ref_urls = { 'list':'references:phone_list', 'create':'references:phone_create', 'detail':'references:phone_detail', 'delete':'references:phone_delete' }

class PhoneListView(LoginRequiredMixin, View):

    template = 'adin/generic_list.html'
    formset = PhoneListModelFormSet
    title = title
    ref_urls = ref_urls
    actions_off = ['update']
    list_order = 'code'
    
    def get(self, request):
        formset = self.formset(queryset=Phone.objects.all().exclude(state=0).order_by(self.list_order))
        context = {'formset': formset, 'title': self.title, 'ref_urls': self.ref_urls, 'actions_off': self.actions_off}
        return render(request, self.template, context)

class PhoneDetailView(GenericDetailView):

    title = title
    model = Phone
    form = PhoneDetailModelForm
    ref_urls = ref_urls
    actions_off = ['update']

class PhoneCreateView(GenericCreateView):

    form = PhoneCreateModelForm
    title = title
    ref_urls = ref_urls

class PhoneDeleteView(GenericDeleteView):

    title = title
    model = Phone
    form = PhoneDeleteModelForm
    ref_urls = ref_urls
    actions_off = ['update']
