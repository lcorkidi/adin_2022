from django.urls import path
from people.views.person_views import PersonListView, PersonCreateView, Person_NaturalCreateView, Person_LegalCreateView, PersonDetailView, Person_NaturalDetailView, Person_LegalDetailView, PersonUpdateView, Person_NaturalUpdateView, Person_LegalUpdateView, PersonDeleteView, Person_NaturalDeleteView, Person_LegalDeleteView
from people.views.person_phone_views import Person_PhoneCreateView, Person_PhoneUpdateView, Person_PhoneDeleteView
from people.views.person_e_mail_views import Person_EmailCreateView, Person_EmailUpdateView, Person_EmailDeleteView
from people.views.person_address_views import Person_AddressCreateView, Person_AddressUpdateView, Person_AddressDeleteView
from people.views.person_legal_person_natural_views import Person_Legal_Person_NaturalCreateView, Person_Legal_Person_NaturalUpdateView, Person_Legal_Person_NaturalDeleteView

app_name = 'people'

urlpatterns = [
    path('person_list', PersonListView.as_view(), name='person_list'),
    path('person_create/', PersonCreateView.as_view(), name='person_create'),
    path('<int:pk>/person_detail/',PersonDetailView.as_view(),name='person_detail'),
    path('<int:pk>/person_update/', PersonUpdateView.as_view(), name='person_update'),
    path('<int:pk>/person_delete/', PersonDeleteView.as_view(), name='person_delete'),
    path('person_natural_create/', Person_NaturalCreateView.as_view(), name='person_natural_create'),
    path('<int:pk>/person_natural_detail/',Person_NaturalDetailView.as_view(),name='person_natural_detail'),
    path('<int:pk>/person_natural_update/', Person_NaturalUpdateView.as_view(), name='person_natural_update'),
    path('<int:pk>/person_natural_delete/', Person_NaturalDeleteView.as_view(), name='person_natural_delete'),
    path('person_legal_create/', Person_LegalCreateView.as_view(), name='person_legal_create'),
    path('<int:pk>/person_legal_detail/',Person_LegalDetailView.as_view(),name='person_legal_detail'),
    path('<int:pk>/person_legal_update/', Person_LegalUpdateView.as_view(), name='person_legal_update'),
    path('<int:pk>/person_legal_delete/', Person_LegalDeleteView.as_view(), name='person_legal_delete'),
    path('<int:pk>/person_phone_create/', Person_PhoneCreateView.as_view(), name='person_phone_create'),
    path('<int:ret_pk>/<int:pk>/person_phone_update/', Person_PhoneUpdateView.as_view(), name='person_phone_update'),
    path('<int:ret_pk>/<int:pk>/person_phone_delete/', Person_PhoneDeleteView.as_view(), name='person_phone_delete'),
    path('<int:pk>/person_e_mail_create/', Person_EmailCreateView.as_view(), name='person_e_mail_create'),
    path('<int:ret_pk>/<int:pk>/person_e_mail_delete/', Person_EmailDeleteView.as_view(), name='person_e_mail_delete'),
    path('<int:ret_pk>/<int:pk>/person_e_mail_update/', Person_EmailUpdateView.as_view(), name='person_e_mail_update'),
    path('<int:pk>/person_address_create/', Person_AddressCreateView.as_view(), name='person_address_create'),
    path('<int:ret_pk>/<int:pk>/person_address_update/', Person_AddressUpdateView.as_view(), name='person_address_update'),
    path('<int:ret_pk>/<int:pk>/person_address_delete/', Person_AddressDeleteView.as_view(), name='person_address_delete'),
    path('<int:pk>/person_legal_person_natural_create/', Person_Legal_Person_NaturalCreateView.as_view(), name='person_legal_person_natural_create'),
    path('<int:ret_pk>/<int:pk>/person_legal_person_natural_update/', Person_Legal_Person_NaturalUpdateView.as_view(), name='person_legal_person_natural_update'),
    path('<int:ret_pk>/<int:pk>/person_legal_person_natural_delete/', Person_Legal_Person_NaturalDeleteView.as_view(), name='person_legal_person_naturaldelete'),
]
