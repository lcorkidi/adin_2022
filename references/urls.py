from django.urls import path
from .views.address_views import AddressListView, AddressListSomeView, AddressListAllView, AddressDetailView, AddressCreateView, AddressDeleteView, AddressActivateView
from .views.phone_views import PhoneListView, PhoneListSomeView, PhoneListAllView, PhoneDetailView, PhoneCreateView, PhoneDeleteView, PhoneActivateView
from .views.e_mail_views import E_MailListView, E_MailListSomeView, E_MailListAllView, E_MailDetailView, E_MailCreateView, E_MailDeleteView, E_MailActivateView
from .views.puc_views import PUCListView,  PUCCreateView, PUCDeleteView

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
    path('puc_list/', PUCListView.as_view(), name='puc_list'),
    path('puc_create/', PUCCreateView.as_view(), name='puc_create'),
    path('puc_delete/', PUCDeleteView.as_view(), name='puc_delete'),
]
