from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from adin.core.views import GenericDetailView, GenerricCreateView, GenericDeleteView
from references.models import Address
from references.forms.address_forms import AddressDetailModelForm, AddressCreateModelForm, AddressDeleteModelForm, AddressListModelFormSet

title = Address._meta.verbose_name_plural
ref_urls = { 'list':'references:address_list', 'create':'references:address_create', 'detail':'references:address_detail', 'delete':'references:address_delete' }

class AddressListView(LoginRequiredMixin, View):

    template = 'adin/generic_list.html'
    formset = AddressListModelFormSet
    title = title
    ref_urls = ref_urls
    actions_off = ['update']
    list_order = 'code'
    
    def get(self, request):
        formset = self.formset(queryset=Address.objects.all().exclude(state=0).order_by(self.list_order))
        context = {'formset': formset, 'title': self.title, 'ref_urls': self.ref_urls, 'actions_off': self.actions_off}
        return render(request, self.template, context)

class AddressDetailView(GenericDetailView):

    title = title
    model = Address
    form = AddressDetailModelForm
    ref_urls = ref_urls
    actions_off = ['update']

class AddressCreateView(GenerricCreateView):

    form = AddressCreateModelForm
    title = title
    ref_urls = ref_urls

class AddressDeleteView(GenericDeleteView):

    title = title
    model = Address
    form = AddressDeleteModelForm
    ref_urls = ref_urls
    actions_off = ['update']
