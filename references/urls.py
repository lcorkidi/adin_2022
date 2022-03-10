from django.urls import path
from .views.address_views import AddressListView, AddressDetailView, AddressCreateView, AddressDeleteView
from .views.phone_views import PhoneListView, PhoneDetailView, PhoneCreateView, PhoneDeleteView
from .views.e_mail_views import E_MailListView, E_MailDetailView, E_MailCreateView, E_MailDeleteView

app_name = 'references'

urlpatterns = [
    path('address_list/', AddressListView.as_view(), name='address_list'),
    path('address_create/', AddressCreateView.as_view(), name='address_create'),
    path('<str:pk>/address_detail/', AddressDetailView.as_view(), name='address_detail'),
    path('<str:pk>/address_delete/', AddressDeleteView.as_view(), name='address_delete'),
    path('phone_list/', PhoneListView.as_view(), name='phone_list'),
    path('phone_create/', PhoneCreateView.as_view(), name='phone_create'),
    path('<str:pk>/phone_detail/', PhoneDetailView.as_view(), name='phone_detail'),
    path('<str:pk>/phone_delete/', PhoneDeleteView.as_view(), name='phone_delete'),
    path('e_mail_list/', E_MailListView.as_view(), name='e_mail_list'),
    path('e_mail_create/', E_MailCreateView.as_view(), name='e_mail_create'),
    path('<str:pk>/e_mail_detail/', E_MailDetailView.as_view(), name='e_mail_detail'),
    path('<str:pk>/e_mail_delete/', E_MailDeleteView.as_view(), name='e_mail_delete'),
]
