from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from reports.forms.charge_report_forms import ChargeReportFormSet
from reports.utils import get_ledger_db, df_to_dict
from home.utils import user_group_str

class ChargeReportView(LoginRequiredMixin, PermissionRequiredMixin, View):
    
    template = 'reports/charge_report.html'
    formset = ChargeReportFormSet
    title = 'Reporte Movimientos'
    permission_required = 'accounting.view_charge'
    
    def get(self, request, acc, fld):
        print(acc, fld)
        formset = self.formset(initial=df_to_dict(get_ledger_db()))
        context = {'formset': formset, 'title': self.title, 'group': user_group_str(request.user)}
        return render(request, self.template, context)
