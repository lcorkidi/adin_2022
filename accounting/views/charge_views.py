from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from accounting.forms.charge_forms import ChargeReportFormSet
from accounting.models import Charge

class ChargeReportView(LoginRequiredMixin, PermissionRequiredMixin, View):
    
    template = 'accounting/charge_report.html'
    formset = ChargeReportFormSet
    title = 'Reporte Movimientos'
    permission_required = 'accounting.view_charge'
    
    def get(self, request):
        charges = Charge.objects\
                        .values('ledger', 'ledger__date', 'ledger__third_party', 'concept__accountable', 'concept__transaction_type', 'concept__date', 'account', 'value')
        formset = self.formset(initial=charges)
        context = {'formset': formset, 'title': self.title}
        return render(request, self.template, context)
