from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models.functions import Cast
from django.db.models.fields import CharField

from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericUpdateView, GenericDeleteView, GenericActivateView
from accounting.forms.account_forms import AccountCreateForm, AccountDetailForm, AccountUpdateForm, AccountDeleteForm, AccountActivateForm, AccountListModelFormSet
from accounting.models import Account
from accounting.utils import GetActionsOn, GetIncludedStates

title = Account._meta.verbose_name_plural
ref_urls = { 'list':'accounting:account_list', 'create':'accounting:account_create', 'detail':'accounting:account_detail', 'update':'accounting:account_update', 'delete':'accounting:account_delete', 'activate':'accounting:account_activate' }

class AccountListView(LoginRequiredMixin, PermissionRequiredMixin, View):

    template = 'adin/generic_list.html'
    formset = AccountListModelFormSet
    model = Account
    title = title
    ref_urls = ref_urls
    actions_on = GetActionsOn
    permission_required = 'accounting.view_account'
    include_states = GetIncludedStates
    
    def get(self, request):
        include_states = self.include_states(request.user, self.model.__name__)
        actions_on = self.actions_on(request.user, self.model.__name__)
        formset = self.formset(queryset=Account.objects.filter(state__in=include_states).annotate(char_code=Cast('code', CharField())).order_by('char_code'))
        context = {'formset': formset, 'title': self.title, 'ref_urls': self.ref_urls, 'actions_on': actions_on}
        return render(request, self.template, context)

class AccountCreateView(GenericCreateView):

    template = 'adin/generic_create.html'
    form = AccountCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    permission_required = 'accounting.add_account'

class AccountDetailView(GenericDetailView):

    title = title
    model = Account
    form = AccountDetailForm
    ref_urls = ref_urls
    permission_required = 'accounting.view_account'

class AccountUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'accounting.change_account'

    def get(self, request, pk):
        if request.user.has_perm('accounting.activate_account'):
            return redirect('accounting:account_update_all', pk)
        else: 
            return redirect('accounting:account_update_some', pk)

class AccountUpdateSomeView(GenericUpdateView):

    model = Account
    form = AccountUpdateForm
    title = title
    ref_urls = ref_urls
    readonly_fields = ['code']
    permission_required = 'accounting.change_account'

class AccountUpdateAllView(GenericUpdateView):

    model = Account
    form = AccountUpdateForm
    title = title
    ref_urls = ref_urls
    readonly_fields = ['code']
    permission_required = 'accounting.activate_account'
    include_states = [ 0, 1, 2, 3 ]

class AccountDeleteView(GenericDeleteView):

    title = title
    model = Account
    form = AccountDeleteForm
    ref_urls = ref_urls
    permission_required = 'accounting.delete_account'

class AccountActivateView(GenericActivateView):

    title = title
    model = Account
    form = AccountActivateForm
    ref_urls = ref_urls
    permission_required = 'accounting.activate_account'
