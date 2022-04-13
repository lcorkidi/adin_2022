from django.urls import path

from accounting.views.account_views import AccountListView, AccountListSomeView, AccountListAllView, AccountCreateView, AccountDetailView, AccountUpdateView, AccountUpdateSomeView, AccountUpdateAllView, AccountDeleteView, AccountActivateView
from accounting.views.ledger_views  import LedgerListView, LedgerListSomeView, LedgerListAllView, LedgerCreateView, LedgerDetailView, LedgerDeleteView, LedgerActivateView
from accounting.views.ledger_type_views import Ledger_TypeListView, Ledger_TypeListSomeView, Ledger_TypeListAllView, Ledger_TypeCreateView, Ledger_TypeDetailView, Ledger_TypeDeleteView, Ledger_TypeActivateView
from accounting.views.charge_concept_views import Charge_ConceptListView, Charge_ConceptListSomeView, Charge_ConceptListAllView, Charge_ConceptCreateView, Charge_ConceptDetailView, Charge_ConceptDeleteView, Charge_ConceptActivateView
from accounting.views.ledger_template_views  import Ledger_TemplateListView, Ledger_TemplateListSomeView, Ledger_TemplateListAllView, Ledger_TemplateCreateView, Ledger_TemplateDetailView, Ledger_TemplateDeleteView, Ledger_TemplateActivateView


app_name = 'accounting'

urlpatterns = [
    path('account_list', AccountListView.as_view(), name='account_list'),
    path('account_list_some', AccountListSomeView.as_view(), name='account_list_some'),
    path('account_list_all', AccountListAllView.as_view(), name='account_list_all'),
    path('account_create/', AccountCreateView.as_view(), name='account_create'),
    path('<int:pk>/account_detail/',AccountDetailView.as_view(),name='account_detail'),
    path('<int:pk>/account_update/', AccountUpdateView.as_view(), name='account_update'),
    path('<int:pk>/account_update_some/', AccountUpdateSomeView.as_view(), name='account_update_some'),
    path('<int:pk>/account_update_all/', AccountUpdateAllView.as_view(), name='account_update_all'),
    path('<int:pk>/account_delete/', AccountDeleteView.as_view(), name='account_delete'),
    path('<int:pk>/account_activate/', AccountActivateView.as_view(), name='account_activate'),
    path('ledger_list', LedgerListView.as_view(), name='ledger_list'), 
    path('ledger_list_some', LedgerListSomeView.as_view(), name='ledger_list_some'), 
    path('ledger_list_all', LedgerListAllView.as_view(), name='ledger_list_all'), 
    path('ledger_create/', LedgerCreateView.as_view(), name='ledger_create'),
    path('<str:pk>/ledger_detail/', LedgerDetailView.as_view(),name='ledger_detail'),
    path('<str:pk>/ledger_delete/', LedgerDeleteView.as_view(), name='ledger_delete'),
    path('<str:pk>/ledger_activate/', LedgerActivateView.as_view(), name='ledger_activate'),
    path('ledger_type_list', Ledger_TypeListView.as_view(), name='ledger_type_list'), 
    path('ledger_type_list_some', Ledger_TypeListSomeView.as_view(), name='ledger_type_list_some'), 
    path('ledger_type_list_all', Ledger_TypeListAllView.as_view(), name='ledger_type_list_all'), 
    path('ledger_type_create/', Ledger_TypeCreateView.as_view(), name='ledger_type_create'),
    path('<str:pk>/ledger_type_detail/', Ledger_TypeDetailView.as_view(),name='ledger_type_detail'),
    path('<str:pk>/ledger_type_delete/', Ledger_TypeDeleteView.as_view(), name='ledger_type_delete'),
    path('<str:pk>/ledger_type_activate/', Ledger_TypeActivateView.as_view(), name='ledger_type_activate'),
    path('charge_concept_list', Charge_ConceptListView.as_view(), name='charge_concept_list'), 
    path('charge_concept_list_some', Charge_ConceptListSomeView.as_view(), name='charge_concept_list_some'), 
    path('charge_concept_list_all', Charge_ConceptListAllView.as_view(), name='charge_concept_list_all'), 
    path('charge_concept_create/', Charge_ConceptCreateView.as_view(), name='charge_concept_create'),
    path('<str:pk>/charge_concept_detail/', Charge_ConceptDetailView.as_view(),name='charge_concept_detail'),
    path('<str:pk>/charge_concept_delete/', Charge_ConceptDeleteView.as_view(), name='charge_concept_delete'),
    path('<str:pk>/charge_concept_activate/', Charge_ConceptActivateView.as_view(), name='charge_concept_activate'),
    path('ledger_template_list', Ledger_TemplateListView.as_view(), name='ledger_template_list'), 
    path('ledger_template_list_some', Ledger_TemplateListSomeView.as_view(), name='ledger_template_list_some'), 
    path('ledger_template_list_all', Ledger_TemplateListAllView.as_view(), name='ledger_template_list_all'), 
    path('ledger_template_create/', Ledger_TemplateCreateView.as_view(), name='ledger_template_create'),
    path('<str:pk>/ledger_template_detail/', Ledger_TemplateDetailView.as_view(),name='ledger_template_detail'),
    path('<str:pk>/ledger_template_delete/', Ledger_TemplateDeleteView.as_view(), name='ledger_template_delete'),
    path('<str:pk>/ledger_template_activate/', Ledger_TemplateActivateView.as_view(), name='ledger_template_activate'),
]
