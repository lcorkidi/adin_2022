from django.urls import path

from accounting.views.account_views import AccountListView, AccountCreateView, AccountDetailView, AccountUpdateView, AccountUpdateSomeView, AccountUpdateAllView, AccountDeleteView, AccountActivateView
from accounting.views.ledger_views  import LedgerListView, LedgerCreateView, LedgerDetailView, LedgerDeleteView, LedgerActivateView
from accounting.views.ledger_type_views import Ledger_TypeListView, Ledger_TypeCreateView, Ledger_TypeDetailView, Ledger_TypeDeleteView, Ledger_TypeActivateView
from accounting.views.ledger_template_views  import Ledger_TemplateListView, Ledger_TemplateCreateView, Ledger_TemplateDetailView, Ledger_TemplateDeleteView, Ledger_TemplateActivateView, Ledger_TemplateSelectView, Ledger_TemplateSelectAccountableView, Ledger_TemplateSelectConceptDataView, Ledger_TemplateSelectConceptView, Ledger_TemplateRegisterCommitView, Ledger_TemplateRegisterReceiptView

app_name = 'accounting'

urlpatterns = [
    path('account_list', AccountListView.as_view(), name='account_list'),
    path('account_create/', AccountCreateView.as_view(), name='account_create'),
    path('<int:pk>/account_detail/',AccountDetailView.as_view(),name='account_detail'),
    path('<int:pk>/account_update/', AccountUpdateView.as_view(), name='account_update'),
    path('<int:pk>/account_update_some/', AccountUpdateSomeView.as_view(), name='account_update_some'),
    path('<int:pk>/account_update_all/', AccountUpdateAllView.as_view(), name='account_update_all'),
    path('<int:pk>/account_delete/', AccountDeleteView.as_view(), name='account_delete'),
    path('<int:pk>/account_activate/', AccountActivateView.as_view(), name='account_activate'),
    path('ledger_list', LedgerListView.as_view(), name='ledger_list'), 
    path('ledger_create/', LedgerCreateView.as_view(), name='ledger_create'),
    path('<str:pk>/ledger_detail/', LedgerDetailView.as_view(),name='ledger_detail'),
    path('<str:pk>/ledger_delete/', LedgerDeleteView.as_view(), name='ledger_delete'),
    path('<str:pk>/ledger_activate/', LedgerActivateView.as_view(), name='ledger_activate'),
    path('ledger_type_list', Ledger_TypeListView.as_view(), name='ledger_type_list'), 
    path('ledger_type_create/', Ledger_TypeCreateView.as_view(), name='ledger_type_create'),
    path('<str:pk>/ledger_type_detail/', Ledger_TypeDetailView.as_view(),name='ledger_type_detail'),
    path('<str:pk>/ledger_type_delete/', Ledger_TypeDeleteView.as_view(), name='ledger_type_delete'),
    path('<str:pk>/ledger_type_activate/', Ledger_TypeActivateView.as_view(), name='ledger_type_activate'),
    path('ledger_template_list', Ledger_TemplateListView.as_view(), name='ledger_template_list'), 
    path('ledger_template_create/', Ledger_TemplateCreateView.as_view(), name='ledger_template_create'),
    path('<str:pk>/ledger_template_detail/', Ledger_TemplateDetailView.as_view(),name='ledger_template_detail'),
    path('<str:pk>/ledger_template_delete/', Ledger_TemplateDeleteView.as_view(), name='ledger_template_delete'),
    path('<str:pk>/ledger_template_activate/', Ledger_TemplateActivateView.as_view(), name='ledger_template_activate'),
    path('ledger_template_select/', Ledger_TemplateSelectView.as_view(), name='ledger_template_select'),
    path('<str:pk>/ledger_template_select_accountable/', Ledger_TemplateSelectAccountableView.as_view(), name='ledger_template_select_accountable'),
    path('<str:lt_pk>/<str:acc_pk>/ledger_template_concept_data/', Ledger_TemplateSelectConceptDataView.as_view(), name='ledger_template_concept_data'),
    path('<str:lt_pk>/<str:acc_pk>/ledger_template_select_concept/', Ledger_TemplateSelectConceptView.as_view(), name='ledger_template_select_concept'),
    path('<str:ac_pk>/<str:a_pk>/<str:lt_str>/ledger_template_register_commit/', Ledger_TemplateRegisterCommitView.as_view(), name='ledger_template_register_commit'),
    path('<str:ac_pk>/ledger_template_register_receipt/', Ledger_TemplateRegisterReceiptView.as_view(), name='ledger_template_register_receipt'),
]
