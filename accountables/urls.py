from django.urls import path

from .views.lease_realty_views import Lease_RealtyListView, Lease_RealtyCreateView, Lease_RealtyDetailView, Lease_RealtyUpdateView, Lease_RealtyDeleteView
from .views.lease_realty_realty_views import Lease_Realty_RealtyCreateView, Lease_Realty_RealtyUpdateView, Lease_Realty_RealtyDeleteView
from .views.lease_realty_person_views import Lease_Realty_PersonCreateView, Lease_Realty_PersonUpdateView, Lease_Realty_PersonDeleteView
from .views.date_value_views import Date_ValueCreateView, Date_ValueUpdateView, Date_ValueDeleteView

app_name = 'accountables'

urlpatterns = [
    path('lease_realty_list', Lease_RealtyListView.as_view(), name='lease_realty_list'), 
    path('lease_realty_create/', Lease_RealtyCreateView.as_view(), name='lease_realty_create'),
    path('<str:pk>/lease_realty_detail/', Lease_RealtyDetailView.as_view(),name='lease_realty_detail'),
    path('<str:pk>/lease_realty_update/', Lease_RealtyUpdateView.as_view(), name='lease_realty_update'),
    path('<str:pk>/lease_realty_delete/', Lease_RealtyDeleteView.as_view(), name='lease_realty_delete'),
    path('<str:pk>/lease_realty_realty_create/', Lease_Realty_RealtyCreateView.as_view(), name='lease_realty_realty_create'),
    path('<str:ret_pk>/<str:pk>/lease_realty_realty_update/', Lease_Realty_RealtyUpdateView.as_view(), name='lease_realty_realty_update'),
    path('<str:ret_pk>/<str:pk>/lease_realty_realty_delete/', Lease_Realty_RealtyDeleteView.as_view(), name='lease_realty_realty_delete'),
    path('<str:pk>/lease_realty_person_create/', Lease_Realty_PersonCreateView.as_view(), name='lease_realty_person_create'),
    path('<str:ret_pk>/<str:pk>/lease_realty_person_update/', Lease_Realty_PersonUpdateView.as_view(), name='lease_realty_person_update'),
    path('<str:ret_pk>/<str:pk>/lease_realty_person_delete/', Lease_Realty_PersonDeleteView.as_view(), name='lease_realty_person_delete'),
    path('<str:pk>/date_value_create/', Date_ValueCreateView.as_view(), name='date_value_create'),
    path('<str:ret_pk>/<str:pk>/date_value_update/', Date_ValueUpdateView.as_view(), name='date_value_update'),
    path('<str:ret_pk>/<str:pk>/date_value_delete/', Date_ValueDeleteView.as_view(), name='date_value_delete'),
]
