import datetime
from calendar import monthrange
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from reports.forms.balance_forms import AccountBalanceFormSet
from reports.utils import ledger_from_db, df_to_dict, ledger_balance
from home.utils import user_group_str

class BalanceView(LoginRequiredMixin, PermissionRequiredMixin, View):
    
    template = 'reports/balance.html'
    formset = AccountBalanceFormSet
    title = 'Balance'
    permission_required = 'accounting.view_balance'
    ledger = ledger_from_db()
    today = datetime.date.today()
    
    def get(self, request, lvl, ext, yr, mth):
        if yr == 0:
            yr = self.today.year
        if mth == 0:
            mth = self.today.month
        if ext == 1:
            start_date = datetime.date(year=yr, month=1, day=1)
            end_date = datetime.date(year=yr, 
                month=self.today.month if yr == self.today.year else 12, 
                day=self.today.day if yr == self.today.year else monthrange(yr, mth)[1])
        else:
            start_date = datetime.date(year=yr, month=mth, day=1)
            end_date = datetime.date(year=yr, month=mth, 
                day=self.today.day if mth == self.today.month else monthrange(yr, mth)[1])
        formset = self.formset(initial=df_to_dict(ledger_balance(self.ledger, lvl, start_date, end_date)))
        context = {'formset': formset, 'title': self.title, 'level': lvl, 'extent': ext, 'year': yr, 'month': mth, 'max_dates': {'month': self.today.month if self.today.year == yr else 12, 'year': datetime.date.today().year}, 'group': user_group_str(request.user)}
        return render(request, self.template, context)
