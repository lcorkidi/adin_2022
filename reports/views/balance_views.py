from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from reports.forms.balance_forms import AccountBalanceFormSet
from reports.utils import get_ledger_db, df_to_dict, balance
from home.utils import user_group_str

class BalanceView(LoginRequiredMixin, PermissionRequiredMixin, View):
    
    template = 'reports/balance.html'
    formset = AccountBalanceFormSet
    title = 'Balance'
    permission_required = 'accounting.view_charge'
    
    def get(self, request):
        formset = self.formset(initial=df_to_dict(balance(get_ledger_db())))
        context = {'formset': formset, 'title': self.title, 'group': user_group_str(request.user)}
        return render(request, self.template, context)
