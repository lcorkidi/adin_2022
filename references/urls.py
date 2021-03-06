from django.urls import path
from .views.address_views import AddressListView, AddressListSomeView, AddressListAllView, AddressDetailView, AddressCreateView, AddressDeleteView, AddressActivateView
from .views.phone_views import PhoneListView, PhoneListSomeView, PhoneListAllView, PhoneDetailView, PhoneCreateView, PhoneDeleteView, PhoneActivateView
from .views.e_mail_views import E_MailListView, E_MailListSomeView, E_MailListAllView, E_MailDetailView, E_MailCreateView, E_MailDeleteView, E_MailActivateView
from .views.transaction_type_views import Transaction_TypeListView, Transaction_TypeListSomeView, Transaction_TypeListAllView, Transaction_TypeCreateView, Transaction_TypeDetailView, Transaction_TypeDeleteView, Transaction_TypeActivateView
from .views.puc_views import PUCListView,  PUCCreateView, PUCDeleteView
from .views.charge_factor_views import Factor_DataListView, Factor_DataListSomeView, Factor_DataListAllView, Charge_FactorCreateView, Factor_DataCreateView, Factor_DataDetailView, Factor_DataDeleteView, Factor_DataActivateView

app_name = 'references'

urlpatterns = [
    path('address_list/', AddressListView.as_view(), name='address_list'),
    path('address_list_some/', AddressListSomeView.as_view(), name='address_list_some'),
    path('address_list_all/', AddressListAllView.as_view(), name='address_list_all'),
    path('address_create/', AddressCreateView.as_view(), name='address_create'),
    path('<str:pk>/address_detail/', AddressDetailView.as_view(), name='address_detail'),
    path('<str:pk>/address_delete/', AddressDeleteView.as_view(), name='address_delete'),
    path('<str:pk>/address_activate/', AddressActivateView.as_view(), name='address_activate'),
    path('phone_list/', PhoneListView.as_view(), name='phone_list'),
    path('phone_list_some/', PhoneListSomeView.as_view(), name='phone_list_some'),
    path('phone_list_all/', PhoneListAllView.as_view(), name='phone_list_all'),
    path('phone_create/', PhoneCreateView.as_view(), name='phone_create'),
    path('<str:pk>/phone_detail/', PhoneDetailView.as_view(), name='phone_detail'),
    path('<str:pk>/phone_delete/', PhoneDeleteView.as_view(), name='phone_delete'),
    path('<str:pk>/phone_activate/', PhoneActivateView.as_view(), name='phone_activate'),
    path('e_mail_list/', E_MailListView.as_view(), name='e_mail_list'),
    path('e_mail_list_some/', E_MailListSomeView.as_view(), name='e_mail_list_some'),
    path('e_mail_list_all/', E_MailListAllView.as_view(), name='e_mail_list_all'),
    path('e_mail_create/', E_MailCreateView.as_view(), name='e_mail_create'),
    path('<str:pk>/e_mail_detail/', E_MailDetailView.as_view(), name='e_mail_detail'),
    path('<str:pk>/e_mail_delete/', E_MailDeleteView.as_view(), name='e_mail_delete'),
    path('<str:pk>/e_mail_activate/', E_MailActivateView.as_view(), name='e_mail_activate'),
    path('transaction_type_list/', Transaction_TypeListView.as_view(), name='transaction_type_list'),
    path('transaction_type_list_some/', Transaction_TypeListSomeView.as_view(), name='transaction_type_list_some'),
    path('transaction_type_list_all/', Transaction_TypeListAllView.as_view(), name='transaction_type_list_all'),
    path('transaction_type_create/', Transaction_TypeCreateView.as_view(), name='transaction_type_create'),
    path('<str:pk>/transaction_type_detail/', Transaction_TypeDetailView.as_view(), name='transaction_type_detail'),
    path('<str:pk>/transaction_type_delete/', Transaction_TypeDeleteView.as_view(), name='transaction_type_delete'),
    path('<str:pk>/transaction_type_activate/', Transaction_TypeActivateView.as_view(), name='transaction_type_activate'),
    path('puc_list/', PUCListView.as_view(), name='puc_list'),
    path('puc_create/', PUCCreateView.as_view(), name='puc_create'),
    path('puc_delete/', PUCDeleteView.as_view(), name='puc_delete'),
    path('factor_data_list/', Factor_DataListView.as_view(), name='factor_data_list'),
    path('factor_data_some/', Factor_DataListSomeView.as_view(), name='factor_data_list_some'),
    path('factor_data_all/', Factor_DataListAllView.as_view(), name='factor_data_list_all'),
    path('charge_factor_create/', Charge_FactorCreateView.as_view(), name='charge_factor_create'),
    path('<str:rel_pk>/factor_data_create/', Factor_DataCreateView.as_view(), name='factor_data_create'),
    path('<str:pk>/factor_data_detail/', Factor_DataDetailView.as_view(), name='factor_data_detail'),
    path('<str:pk>/factor_data_delete/', Factor_DataDeleteView.as_view(), name='factor_data_delete'),
    path('<str:pk>/factor_data_activate/', Factor_DataActivateView.as_view(), name='factor_data_activate'),
]
