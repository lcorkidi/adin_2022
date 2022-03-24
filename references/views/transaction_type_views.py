from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView, GenericActivateView
from references.models import Transaction_Type
from references.forms.transaction_type_forms import Transaction_TypeDetailModelForm, Transaction_TypeCreateModelForm, Transaction_TypeDeleteModelForm, Transaction_TypeListModelFormSet

title = Transaction_Type._meta.verbose_name_plural
ref_urls = { 'list':'references:transaction_type_list', 'create':'references:transaction_type_create', 'detail':'references:transaction_type_detail', 'delete':'references:transaction_type_delete', 'activate':'references:transaction_type_activate' }

class Transaction_TypeListView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'references.view_transaction_type'

    def get(self, request):
        if request.user.has_perm('references.activate_transaction_type'):
            return redirect('references:transaction_type_list_all')
        else: 
            return redirect('references:transaction_type_list_some')

class Transaction_TypeListSomeView(GenericListView):

    template = 'adin/generic_list.html'
    formset = Transaction_TypeListModelFormSet
    model = Transaction_Type
    title = title
    ref_urls = ref_urls
    actions_off = ['update']
    list_order = 'transaction_type'
    permission_required = 'references.view_transaction_type'

class Transaction_TypeListAllView(GenericListView):

    template = 'adin/generic_list.html'
    formset = Transaction_TypeListModelFormSet
    model = Transaction_Type
    title = title
    ref_urls = ref_urls
    actions_off = ['update']
    list_order = 'name'
    permission_required = 'references.activate_transaction_type'
    include_states = [ 0, 1, 2, 3 ]

class Transaction_TypeCreateView(GenericCreateView):

    form = Transaction_TypeCreateModelForm
    title = title
    ref_urls = ref_urls
    permission_required = 'references.add_transaction_type'

class Transaction_TypeDetailView(GenericDetailView):

    title = title
    model = Transaction_Type
    form = Transaction_TypeDetailModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'references.view_transaction_type'

class Transaction_TypeDeleteView(GenericDeleteView):

    title = title
    model = Transaction_Type
    form = Transaction_TypeDeleteModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'references.delete_transaction_type'

class Transaction_TypeActivateView(GenericActivateView):

    title = title
    model = Transaction_Type
    form = Transaction_TypeDeleteModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'references.activate_transaction_type'
