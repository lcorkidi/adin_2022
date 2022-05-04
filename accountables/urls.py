from django.urls import path

from .views.lease_realty_views import Lease_RealtyListView, Lease_RealtyListSomeView, Lease_RealtyListAllView, Lease_RealtyCreateView, Lease_RealtyDetailView, Lease_RealtyUpdateView, Lease_RealtyUpdateSomeView, Lease_RealtyUpdateAllView, Lease_RealtyAccountingView, Lease_RealtyDeleteView, Lease_RealtyActivateView
from .views.lease_realty_realty_views import Lease_Realty_RealtyCreateView, Lease_Realty_RealtyUpdateView, Lease_Realty_RealtyDeleteView, Lease_Realty_RealtyActivateView
from .views.lease_realty_person_views import Lease_Realty_PersonCreateView, Lease_Realty_PersonUpdateView, Lease_Realty_PersonDeleteView, Lease_Realty_PersonActivateView
from .views.lease_realty_trasaction_type_views import Lease_Realty_Transaction_TypeAddView, Lease_Realty_Transaction_TypeRemoveView
from .views.date_value_views import Date_ValueCreateView, Date_ValueUpdateView, Date_ValueDeleteView, Date_ValueActivateView

app_name = 'accountables'

urlpatterns = [
    path('lease_realty_list', Lease_RealtyListView.as_view(), name='lease_realty_list'), 
    path('lease_realty_list_some', Lease_RealtyListSomeView.as_view(), name='lease_realty_list_some'), 
    path('lease_realty_list_all', Lease_RealtyListAllView.as_view(), name='lease_realty_list_all'), 
    path('lease_realty_create/', Lease_RealtyCreateView.as_view(), name='lease_realty_create'),
    path('<str:pk>/lease_realty_detail/', Lease_RealtyDetailView.as_view(),name='lease_realty_detail'),
    path('<str:pk>/lease_realty_update/', Lease_RealtyUpdateView.as_view(), name='lease_realty_update'),
    path('<str:pk>/lease_realty_update_some/', Lease_RealtyUpdateSomeView.as_view(), name='lease_realty_update_some'),
    path('<str:pk>/lease_realty_accounting/', Lease_RealtyAccountingView.as_view(), name='lease_realty_accounting'),
    path('<str:pk>/lease_realty_update_all/', Lease_RealtyUpdateAllView.as_view(), name='lease_realty_update_all'),
    path('<str:pk>/lease_realty_delete/', Lease_RealtyDeleteView.as_view(), name='lease_realty_delete'),
    path('<str:pk>/lease_realty_activate/', Lease_RealtyActivateView.as_view(), name='lease_realty_activate'),
    path('<str:pk>/lease_realty_realty_create/', Lease_Realty_RealtyCreateView.as_view(), name='lease_realty_realty_create'),
    path('<str:ret_pk>/<str:pk>/lease_realty_realty_update/', Lease_Realty_RealtyUpdateView.as_view(), name='lease_realty_realty_update'),
    path('<str:ret_pk>/<str:pk>/lease_realty_realty_delete/', Lease_Realty_RealtyDeleteView.as_view(), name='lease_realty_realty_delete'),
    path('<str:ret_pk>/<str:pk>/lease_realty_realty_activate/', Lease_Realty_RealtyActivateView.as_view(), name='lease_realty_realty_activate'),
    path('<str:pk>/lease_realty_person_create/', Lease_Realty_PersonCreateView.as_view(), name='lease_realty_person_create'),
    path('<str:ret_pk>/<str:pk>/lease_realty_person_update/', Lease_Realty_PersonUpdateView.as_view(), name='lease_realty_person_update'),
    path('<str:ret_pk>/<str:pk>/lease_realty_person_delete/', Lease_Realty_PersonDeleteView.as_view(), name='lease_realty_person_delete'),
    path('<str:ret_pk>/<str:pk>/lease_realty_person_activate/', Lease_Realty_PersonActivateView.as_view(), name='lease_realty_person_activate'),
    path('<str:pk>/lease_realty_transaction_type_add/', Lease_Realty_Transaction_TypeAddView.as_view(), name='lease_realty_transaction_type_add'),
    path('<str:pk>/lease_realty_transaction_type_remove/', Lease_Realty_Transaction_TypeRemoveView.as_view(), name='lease_realty_transaction_type_remove'),
    path('<str:pk>/date_value_create/', Date_ValueCreateView.as_view(), name='date_value_create'),
    path('<str:ret_pk>/<str:pk>/date_value_update/', Date_ValueUpdateView.as_view(), name='date_value_update'),
    path('<str:ret_pk>/<str:pk>/date_value_delete/', Date_ValueDeleteView.as_view(), name='date_value_delete'),
    path('<str:ret_pk>/<str:pk>/date_value_activate/', Date_ValueActivateView.as_view(), name='date_value_activate'),
]
