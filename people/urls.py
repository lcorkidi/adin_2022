from django.urls import path
from people.views.person_views import PersonListView, PersonCreateView, Person_NaturalCreateView, Person_LegalCreateView, PersonDetailView, Person_NaturalDetailView, Person_LegalDetailView, PersonUpdateView, Person_NaturalUpdateSomeView, Person_NaturalUpdateAllView, Person_LegalUpdateSomeView, Person_LegalUpdateAllView, PersonDeleteView, Person_NaturalDeleteView, Person_LegalDeleteView, PersonActivateView, Person_NaturalActivateView, Person_LegalActivateView
from people.views.person_phone_views import Person_PhoneCreateView, Person_PhoneUpdateView, Person_PhoneDeleteView, Person_PhoneActivateView
from people.views.person_e_mail_views import Person_EmailCreateView, Person_EmailUpdateView, Person_EmailDeleteView, Person_EmailActivateView
from people.views.person_address_views import Person_AddressCreateView, Person_AddressUpdateView, Person_AddressDeleteView, Person_AddressActivateView
from people.views.person_legal_person_natural_views import Person_Legal_Person_NaturalCreateView, Person_Legal_Person_NaturalUpdateView, Person_Legal_Person_NaturalDeleteView, Person_Legal_Person_NaturalActivateView

app_name = 'people'

urlpatterns = [
    path('person_list', PersonListView.as_view(), name='person_list'),
    path('person_create/', PersonCreateView.as_view(), name='person_create'),
    path('<int:pk>/person_detail/',PersonDetailView.as_view(),name='person_detail'),
    path('<int:pk>/person_update/', PersonUpdateView.as_view(), name='person_update'),
    path('<int:pk>/person_delete/', PersonDeleteView.as_view(), name='person_delete'),
    path('<int:pk>/person_activate/', PersonActivateView.as_view(), name='person_activate'),
    path('person_natural_create/', Person_NaturalCreateView.as_view(), name='person_natural_create'),
    path('<int:pk>/person_natural_detail/',Person_NaturalDetailView.as_view(),name='person_natural_detail'),
    path('<int:pk>/person_natural_update_some/', Person_NaturalUpdateSomeView.as_view(), name='person_natural_update_some'),
    path('<int:pk>/person_natural_update_all/', Person_NaturalUpdateAllView.as_view(), name='person_natural_update_all'),
    path('<int:pk>/person_natural_delete/', Person_NaturalDeleteView.as_view(), name='person_natural_delete'),
    path('<int:pk>/person_natural_activate/', Person_NaturalActivateView.as_view(), name='person_natural_activate'),
    path('person_legal_create/', Person_LegalCreateView.as_view(), name='person_legal_create'),
    path('<int:pk>/person_legal_detail/',Person_LegalDetailView.as_view(),name='person_legal_detail'),
    path('<int:pk>/person_legal_update_some/', Person_LegalUpdateSomeView.as_view(), name='person_legal_update_some'),
    path('<int:pk>/person_legal_update_all/', Person_LegalUpdateAllView.as_view(), name='person_legal_update_all'),
    path('<int:pk>/person_legal_delete/', Person_LegalDeleteView.as_view(), name='person_legal_delete'),
    path('<int:pk>/person_legal_activate/', Person_LegalActivateView.as_view(), name='person_legal_activate'),
    path('<int:pk>/person_phone_create/', Person_PhoneCreateView.as_view(), name='person_phone_create'),
    path('<int:ret_pk>/<int:pk>/person_phone_update/', Person_PhoneUpdateView.as_view(), name='person_phone_update'),
    path('<int:ret_pk>/<int:pk>/person_phone_delete/', Person_PhoneDeleteView.as_view(), name='person_phone_delete'),
    path('<int:ret_pk>/<int:pk>/person_phone_activate/', Person_PhoneActivateView.as_view(), name='person_phone_activate'),
    path('<int:pk>/person_e_mail_create/', Person_EmailCreateView.as_view(), name='person_e_mail_create'),
    path('<int:ret_pk>/<int:pk>/person_e_mail_update/', Person_EmailUpdateView.as_view(), name='person_e_mail_update'),
    path('<int:ret_pk>/<int:pk>/person_e_mail_delete/', Person_EmailDeleteView.as_view(), name='person_e_mail_delete'),
    path('<int:ret_pk>/<int:pk>/person_e_mail_activate/', Person_EmailActivateView.as_view(), name='person_e_mail_activate'),
    path('<int:pk>/person_address_create/', Person_AddressCreateView.as_view(), name='person_address_create'),
    path('<int:ret_pk>/<int:pk>/person_address_update/', Person_AddressUpdateView.as_view(), name='person_address_update'),
    path('<int:ret_pk>/<int:pk>/person_address_delete/', Person_AddressDeleteView.as_view(), name='person_address_delete'),
    path('<int:ret_pk>/<int:pk>/person_address_activate/', Person_AddressActivateView.as_view(), name='person_address_activate'),
    path('<int:pk>/person_legal_person_natural_create/', Person_Legal_Person_NaturalCreateView.as_view(), name='person_legal_person_natural_create'),
    path('<int:ret_pk>/<int:pk>/person_legal_person_natural_update/', Person_Legal_Person_NaturalUpdateView.as_view(), name='person_legal_person_natural_update'),
    path('<int:ret_pk>/<int:pk>/person_legal_person_natural_delete/', Person_Legal_Person_NaturalDeleteView.as_view(), name='person_legal_person_natural_delete'),
    path('<int:ret_pk>/<int:pk>/person_legal_person_natural_activate/', Person_Legal_Person_NaturalActivateView.as_view(), name='person_legal_person_natural_activate'),
]
