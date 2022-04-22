import datetime
from calendar import monthrange
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from reports.forms.balance_forms import AccountBalanceForm
from reports.forms.charge_report_forms import ChargeReportFormSet
from reports.utils import ledger_from_db, account_balance, account_charges, df_to_dict
from home.utils import user_group_str
from accounting.core.structure import Account_Structure

class AccountReportView(LoginRequiredMixin, PermissionRequiredMixin, View):
    
    template = 'reports/account_report.html'
    form = AccountBalanceForm
    formset = ChargeReportFormSet
    title = 'Reporte Movimientos'
    permission_required = 'accounting.view_charge'
    ledger = ledger_from_db()
    today = datetime.date.today()
    
    def get(self, request, acc, fld, ext, yr, mth):
        if yr == 0:
            yr = self.today.year
        if mth == 0:
            mth = self.today.month
        if ext == 1:
            start_date = datetime.date(year=yr, month=1, day=1)
            end_date = datetime.date(year=yr, 
                month=self.today.month if yr == self.today.year else 12, 
                day=self.today.day if yr == self.today.year else monthrange(yr, mth)[1])
        elif ext == 0:
            start_date = datetime.date(year=yr, month=mth, day=1)
            end_date = datetime.date(year=yr, month=mth, 
                day=self.today.day if mth == self.today.month else monthrange(yr, mth)[1])
        else:
            start_date = datetime.date(2021, 1, 1)
            end_date = datetime.date.today() 
        if fld == 'debit':
            value = 1
        elif fld == 'credit':
            value = -1
        else:
            value = 0
        print(start_date, end_date)
        form = self.form(initial=account_balance(self.ledger, acc, start_date, end_date))
        formset = self.formset(initial=df_to_dict(account_charges(self.ledger, acc, start_date, end_date, value)))
        context = {'form': form, 'formset': formset, 'title': self.title, 'level': Account_Structure.level(acc), 'account': acc, 'field': fld, 'extent': ext, 'year': yr, 'month': mth, 'max_dates': {'month': self.today.month if self.today.year == yr else 12, 'year': datetime.date.today().year}, 'group': user_group_str(request.user)}
        return render(request, self.template, context)
