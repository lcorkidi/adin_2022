from django.urls import path
from .views.calendar_date_views import Calendar_DateListView, Calendar_DateDetailView, Calendar_DateCreateView, Calendar_DateDeleteView, Calendar_DateActivateView
from .views.address_views import AddressListView, AddressDetailView, AddressCreateView, AddressDeleteView, AddressActivateView
from .views.phone_views import PhoneListView, PhoneDetailView, PhoneCreateView, PhoneDeleteView, PhoneActivateView
from .views.e_mail_views import E_MailListView, E_MailDetailView, E_MailCreateView, E_MailDeleteView, E_MailActivateView
from .views.puc_views import PUCListView,  PUCCreateView, PUCDeleteView
from .views.charge_factor_views import Factor_DataListView, Charge_FactorCreateView, Factor_DataCreateView, Factor_DataDetailView, Factor_DataDeleteView, Factor_DataActivateView

app_name = 'references'

urlpatterns = [
    path('calendar_date_list/', Calendar_DateListView.as_view(), name='calendar_date_list'),
    path('calendar_date_create/', Calendar_DateCreateView.as_view(), name='calendar_date_create'),
    path('<str:pk>/calendar_date_detail/', Calendar_DateDetailView.as_view(), name='calendar_date_detail'),
    path('<str:pk>/calendar_date_delete/', Calendar_DateDeleteView.as_view(), name='calendar_date_delete'),
    path('<str:pk>/calendar_date_activate/', Calendar_DateActivateView.as_view(), name='calendar_date_activate'),
    path('address_list/', AddressListView.as_view(), name='address_list'),
    path('address_create/', AddressCreateView.as_view(), name='address_create'),
    path('<str:pk>/address_detail/', AddressDetailView.as_view(), name='address_detail'),
    path('<str:pk>/address_delete/', AddressDeleteView.as_view(), name='address_delete'),
    path('<str:pk>/address_activate/', AddressActivateView.as_view(), name='address_activate'),
    path('phone_list/', PhoneListView.as_view(), name='phone_list'),
    path('phone_create/', PhoneCreateView.as_view(), name='phone_create'),
    path('<str:pk>/phone_detail/', PhoneDetailView.as_view(), name='phone_detail'),
    path('<str:pk>/phone_delete/', PhoneDeleteView.as_view(), name='phone_delete'),
    path('<str:pk>/phone_activate/', PhoneActivateView.as_view(), name='phone_activate'),
    path('e_mail_list/', E_MailListView.as_view(), name='e_mail_list'),
    path('e_mail_create/', E_MailCreateView.as_view(), name='e_mail_create'),
    path('<str:pk>/e_mail_detail/', E_MailDetailView.as_view(), name='e_mail_detail'),
    path('<str:pk>/e_mail_delete/', E_MailDeleteView.as_view(), name='e_mail_delete'),
    path('<str:pk>/e_mail_activate/', E_MailActivateView.as_view(), name='e_mail_activate'),
    path('puc_list/', PUCListView.as_view(), name='puc_list'),
    path('puc_create/', PUCCreateView.as_view(), name='puc_create'),
    path('puc_delete/', PUCDeleteView.as_view(), name='puc_delete'),
    path('factor_data_list/', Factor_DataListView.as_view(), name='factor_data_list'),
    path('charge_factor_create/', Charge_FactorCreateView.as_view(), name='charge_factor_create'),
    path('<str:rel_pk>/factor_data_create/', Factor_DataCreateView.as_view(), name='factor_data_create'),
    path('<str:pk>/factor_data_detail/', Factor_DataDetailView.as_view(), name='factor_data_detail'),
    path('<str:pk>/factor_data_delete/', Factor_DataDeleteView.as_view(), name='factor_data_delete'),
    path('<str:pk>/factor_data_activate/', Factor_DataActivateView.as_view(), name='factor_data_activate'),
]
