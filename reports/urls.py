from django.urls import path

from .views.charge_report_views import ChargeReportView
from .views.balance_views import BalanceView

app_name = 'reports'

urlpatterns = [
    path('charge_report/', ChargeReportView.as_view(), name='charge_report'),
    path('balance/', BalanceView.as_view(), name='balance'),
]
