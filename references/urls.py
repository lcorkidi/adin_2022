from django.urls import path
from .views import AddressListView, AddressDetailView, AddressCreateView, AddressDeleteView

app_name = 'references'

urlpatterns = [
    path('address_list/', AddressListView.as_view(), name='address_list'),
    path('address_create/', AddressCreateView.as_view(), name='address_create'),
    path('<str:pk>/address_detail/', AddressDetailView.as_view(), name='address_detail'),
    path('<str:pk>/address_delete/', AddressDeleteView.as_view(), name='address_delete'),
]
