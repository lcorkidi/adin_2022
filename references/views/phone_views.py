from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView, GenericActivateView
from references.models import Phone
from references.forms.phone_forms import PhoneDetailModelForm, PhoneCreateModelForm, PhoneDeleteModelForm, PhoneActivateModelForm, PhoneListModelFormSet

title = Phone._meta.verbose_name_plural
ref_urls = { 'list':'references:phone_list', 'create':'references:phone_create', 'detail':'references:phone_detail', 'delete':'references:phone_delete', 'activate':'references:phone_activate' }

class PhoneListView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'references.view_phone'

    def get(self, request):
        if request.user.has_perm('references.activate_phone'):
            return redirect('references:phone_list_all')
        else: 
            return redirect('references:phone_list_some')

class PhoneListSomeView(GenericListView):

    template = 'adin/generic_list.html'
    formset = PhoneListModelFormSet
    model = Phone
    title = title
    ref_urls = ref_urls
    actions_off = ['update']
    list_order = 'code'
    permission_required = 'references.view_phone'

class PhoneListAllView(GenericListView):

    template = 'adin/generic_list.html'
    formset = PhoneListModelFormSet
    model = Phone
    title = title
    ref_urls = ref_urls
    actions_off = ['update']
    list_order = 'code'
    permission_required = 'references.activate_phone'
    include_states = [ 0, 1, 2, 3 ]

class PhoneCreateView(GenericCreateView):

    form = PhoneCreateModelForm
    title = title
    ref_urls = ref_urls
    permission_required = 'references.add_phone'

class PhoneDetailView(GenericDetailView):

    title = title
    model = Phone
    form = PhoneDetailModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'references.view_phone'

class PhoneDeleteView(GenericDeleteView):

    title = title
    model = Phone
    form = PhoneDeleteModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'references.delete_phone'

class PhoneActivateView(GenericActivateView):

    title = title
    model = Phone
    form = PhoneActivateModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'references.activate_phone'
