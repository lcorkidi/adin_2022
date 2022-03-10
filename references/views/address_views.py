from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from adin.core.views import GenericDetailView, GenerricCreateView, GenericDeleteView
from references.models import Address
from references.forms.address_forms import AddressDetailModelForm, AddressCreateModelForm, AddressListModelFormSet

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
    form = AddressDetailModelForm
    ref_urls = ref_urls
    actions_off = ['update']

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        m2m_data = self.m2m_data()
        if form.has_changed():
            if self.m2m_data:
                for attr, data in m2m_data.items():
                    form.set_hidden_field(attr)
                    formset = data['formset'](queryset=data['class'].objects.exclude(state=0).filter(person__id_number=pk))
                    m2m_data[attr]['formset'] = formset
                context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'form':form, 'm2m_data':m2m_data, 'choice_fields':self.choice_fields, 'actions_off': self.actions_off }
                return render(request, self.template, context)
            else:
                m2m_data = None
        for attr, data in m2m_data.items():
            data['class'].objects.exclude(state=0).filter(person__id_number=pk).update(state=0)
        obj.state = 0
        obj.save()
        return redirect(self.ref_urls['list'])
