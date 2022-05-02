from django.urls import path

from .views.balance_views import BalanceView
from .views.account_report_views import AccountReportView

app_name = 'reports'

urlpatterns = [
    path('<int:lvl>/<int:ext>/<int:yr>/<int:mth>/balance/', BalanceView.as_view(), name='balance'),
    path('<int:acc>/<str:fld>/<int:ext>/<int:yr>/<int:mth>/account_report/', AccountReportView.as_view(), name='account_report'),
]
