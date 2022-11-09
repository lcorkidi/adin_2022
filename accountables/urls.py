from django.urls import path

from .views.lease_realty_views import Lease_RealtyMainView, Lease_RealtyListView, Lease_RealtyCreateView, Lease_RealtyDetailView, Lease_RealtyUpdateView, Lease_RealtyAccountingView, Lease_RealtyReportView, Lease_RealtyDeleteView, Lease_RealtyActivateView
from .views.lease_realty_realty_views import Lease_Realty_RealtyCreateView, Lease_Realty_RealtyDeleteView, Lease_Realty_RealtyActivateView
from .views.lease_realty_person_views import Lease_Realty_PersonCreateView, Lease_Realty_PersonDetailView, Lease_Realty_PersonUpdateView, Lease_Realty_PersonDeleteView, Lease_Realty_PersonActivateView
from .views.transaction_type_views import Transaction_TypeListView, Transaction_TypeCreateView, Transaction_TypeDetailView, Transaction_TypeDeleteView, Transaction_TypeActivateView
from .views.accountable_transaction_type_views import Accountable_Transaction_TypeCreateView, Accountable_Transaction_TypeDetailView, Accountable_Transaction_TypeUpdateView, Accountable_Transaction_TypeDeleteiew, Accountable_Transaction_TypeActivateView
from .views.accountable_concept_views import Accountable_ConceptCreateView, Accountable_ConceptAccountableAllPendingCreateView, Accountable_ConceptBulkPendingCreateView, Accountable_ConceptSinglePendingCreateView, Accountable_ConceptDeleteView, Accountable_ConceptActivateView, Accountable_ConceptAccountableAllPendingCreateSelectTransaction_TypeView
from .views.date_value_views import Date_ValueCreateView, Date_ValueUpdateView, Date_ValueDeleteView, Date_ValueActivateView

app_name = 'accountables'

urlpatterns = [
    path('transaction_type_list/', Transaction_TypeListView.as_view(), name='transaction_type_list'),
    path('transaction_type_create/', Transaction_TypeCreateView.as_view(), name='transaction_type_create'),
    path('<str:pk>/transaction_type_detail/', Transaction_TypeDetailView.as_view(), name='transaction_type_detail'),
    path('<str:pk>/transaction_type_delete/', Transaction_TypeDeleteView.as_view(), name='transaction_type_delete'),
    path('<str:pk>/transaction_type_activate/', Transaction_TypeActivateView.as_view(), name='transaction_type_activate'),
    path('lease_realty_main/', Lease_RealtyMainView.as_view(), name='lease_realty_main'), 
    path('lease_realty_list/', Lease_RealtyListView.as_view(), name='lease_realty_list'), 
    path('lease_realty_create/', Lease_RealtyCreateView.as_view(), name='lease_realty_create'),
    path('<str:pk>/lease_realty_detail/', Lease_RealtyDetailView.as_view(),name='lease_realty_detail'),
    path('<str:pk>/lease_realty_update/', Lease_RealtyUpdateView.as_view(), name='lease_realty_update'),
    path('<str:pk>/lease_realty_accounting/', Lease_RealtyAccountingView.as_view(), name='lease_realty_accounting'),
    path('<str:pk>/lease_realty_report/', Lease_RealtyReportView.as_view(), name='lease_realty_report'),
    path('<str:pk>/lease_realty_delete/', Lease_RealtyDeleteView.as_view(), name='lease_realty_delete'),
    path('<str:pk>/lease_realty_activate/', Lease_RealtyActivateView.as_view(), name='lease_realty_activate'),
    path('<str:pk>/lease_realty_realty_create/', Lease_Realty_RealtyCreateView.as_view(), name='lease_realty_realty_create'),
    path('<str:ret_pk>/<str:pk>/lease_realty_realty_delete/', Lease_Realty_RealtyDeleteView.as_view(), name='lease_realty_realty_delete'),
    path('<str:ret_pk>/<str:pk>/lease_realty_realty_activate/', Lease_Realty_RealtyActivateView.as_view(), name='lease_realty_realty_activate'),
    path('<str:pk>/lease_realty_person_create/', Lease_Realty_PersonCreateView.as_view(), name='lease_realty_person_create'),
    path('<str:ret_pk>/<str:pk>/lease_realty_person_detail/', Lease_Realty_PersonDetailView.as_view(), name='lease_realty_person_detail'),
    path('<str:ret_pk>/<str:pk>/lease_realty_person_update/', Lease_Realty_PersonUpdateView.as_view(), name='lease_realty_person_update'),
    path('<str:ret_pk>/<str:pk>/lease_realty_person_delete/', Lease_Realty_PersonDeleteView.as_view(), name='lease_realty_person_delete'),
    path('<str:ret_pk>/<str:pk>/lease_realty_person_activate/', Lease_Realty_PersonActivateView.as_view(), name='lease_realty_person_activate'),
    path('<str:pk>/accountable_transaction_type_create/', Accountable_Transaction_TypeCreateView.as_view(), name='accountable_transaction_type_create'),
    path('<str:ret_pk>/<str:pk>/accountable_transaction_type_detail/', Accountable_Transaction_TypeDetailView.as_view(), name='accountable_transaction_type_detail'),
    path('<str:ret_pk>/<str:pk>/accountable_transaction_type_update/', Accountable_Transaction_TypeUpdateView.as_view(), name='accountable_transaction_type_update'),
    path('<str:ret_pk>/<str:pk>/accountable_transaction_type_delete/', Accountable_Transaction_TypeDeleteiew.as_view(), name='accountable_transaction_type_delete'),
    path('<str:ret_pk>/<str:pk>/accountable_transaction_type_activate/', Accountable_Transaction_TypeActivateView.as_view(), name='accountable_transaction_type_activate'),
    path('<str:pk>/accountable_concept_create/', Accountable_ConceptAccountableAllPendingCreateSelectTransaction_TypeView.as_view(), name='accountable_concept_create'),
    path('<str:pk>/<str:tra_typ>/pending_accountable_concept_create/', Accountable_ConceptAccountableAllPendingCreateView.as_view(), name='pending_accountable_concept_create'),
    path('bulk_pending_accountable_concept_create/', Accountable_ConceptBulkPendingCreateView.as_view(), name='bulk_pending_accountable_concept_create'),
    path('<int:cnt>/single_pending_accountable_concept_create/', Accountable_ConceptSinglePendingCreateView.as_view(), name='single_pending_accountable_concept_create'),
    path('<str:ret_pk>/<str:pk>/accountable_concept_delete/', Accountable_ConceptDeleteView.as_view(), name='accountable_concept_delete'),
    path('<str:ret_pk>/<str:pk>/accountable_concept_activate/', Accountable_ConceptActivateView.as_view(), name='accountable_concept_activate'),
    path('<str:pk>/date_value_create/', Date_ValueCreateView.as_view(), name='date_value_create'),
    path('<str:ret_pk>/<str:pk>/date_value_update/', Date_ValueUpdateView.as_view(), name='date_value_update'),
    path('<str:ret_pk>/<str:pk>/date_value_delete/', Date_ValueDeleteView.as_view(), name='date_value_delete'),
    path('<str:ret_pk>/<str:pk>/date_value_activate/', Date_ValueActivateView.as_view(), name='date_value_activate'),
]
