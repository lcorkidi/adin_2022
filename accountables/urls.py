from django.urls import path

from .views.lease_realty_views import Lease_RealtyListView, Lease_RealtyCreateView, Lease_RealtyDetailView, Lease_RealtyUpdateView, Lease_RealtyDeleteView

app_name = 'accountables'

urlpatterns = [
    path('lease_realty_list', Lease_RealtyListView.as_view(), name='lease_realty_list'), 
    path('lease_realty_create/', Lease_RealtyCreateView.as_view(), name='lease_realty_create'),
    path('<str:pk>/lease_realty_detail/', Lease_RealtyDetailView.as_view(),name='lease_realty_detail'),
    path('<str:pk>/lease_realty_update/', Lease_RealtyUpdateView.as_view(), name='lease_realty_update'),
    path('<str:pk>/lease_realty_delete/', Lease_RealtyDeleteView.as_view(), name='lease_realty_delete'),
]
