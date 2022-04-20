from django.urls import path

from .views.charge_report_views import ChargeReportView
from .views.balance_views import BalanceView

app_name = 'reports'

urlpatterns = [
    path('<int:acc>/<str:fld>/charge_report/', ChargeReportView.as_view(), name='charge_report'),
    path('<int:lvl>/<int:ext>/<int:yr>/<int:mth>/balance/', BalanceView.as_view(), name='balance'),
]
