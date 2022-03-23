from django.shortcuts import render
from django.db.models.functions import Cast
from django.db.models.fields import CharField

from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericUpdateView, GenericDeleteView
from accounting.forms.account_forms import AccountCreateForm, AccountDetailForm, AccountUpdateForm, AccountDeleteForm, AccountListModelFormSet
from accounting.models import Account

title = Account._meta.verbose_name_plural
ref_urls = { 'list':'accounting:account_list', 'create':'accounting:account_create', 'detail':'accounting:account_detail', 'update':'accounting:account_update', 'delete':'accounting:account_delete' }

class AccountListView(GenericListView):

    template = 'adin/generic_list.html'
    formset = AccountListModelFormSet
    model = Account
    title = title
    ref_urls = ref_urls
    permission_required = 'accounting.view_account'
    
    def get(self, request):
        formset = self.formset(queryset=Account.objects.exclude(state=0).annotate(char_code=Cast('code', CharField())).order_by('char_code'))
        context = {'formset': formset, 'title': self.title, 'ref_urls': self.ref_urls, 'choice_fields': self.choice_fields, 'actions_off': self.actions_off}
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

class AccountUpdateView(GenericUpdateView):

    model = Account
    form = AccountUpdateForm
    title = title
    ref_urls = ref_urls
    readonly_fields = ['code']
    permission_required = 'accounting.change_account'

class AccountDeleteView(GenericDeleteView):

    title = title
    model = Account
    form = AccountDeleteForm
    ref_urls = ref_urls
    permission_required = 'accounting.delete_account'
