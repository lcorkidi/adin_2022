from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('', views.PersonListView.as_view(), name='people_list'),
    path('create/', views.PersonCreateView.as_view(), name='people_create'),
    path('create_natural/', views.Person_NaturalCreateView.as_view(), name='people_natural_create'),
    path('create_legal/', views.Person_LegalCreateView.as_view(), name='people_legal_create'),
    path('<int:pk>/create_phone/', views.Person_PhoneCreateView.as_view(), name='people_phone_create'),
    path('<int:pk>/create_email/', views.Peorson_EmailCreateView.as_view(), name='people_email_create'),
    path('<int:pk>/create_address/', views.Person_AddressCreateView.as_view(), name='people_address_create'),
    path('<int:pk>/create_staff/', views.Person_Legal_Person_NaturalCreateView.as_view(), name='people_staff_create'),
    path('<int:pk>/detail/',views.PersonDetailView.as_view(),name='people_detail'),
    path('<int:pk>/detail_natural/',views.Person_NaturalDetailView.as_view(),name='people_natural_detail'),
    path('<int:pk>/detail_legal/',views.Person_LegalDetailView.as_view(),name='people_legal_detail'),
    path('<int:pk>/update/', views.PersonUpdateView.as_view(), name='people_update'),
    path('<int:pk>/update_natural/', views.Person_NaturalUpdateView.as_view(), name='people_natural_update'),
    path('<int:pk>/update_legal/', views.Person_LegalUpdateView.as_view(), name='people_legal_update'),
    path('<int:ret_pk>/<int:pk>/update_phone/', views.Person_PhoneUpdateView.as_view(), name='people_phone_update'),
    path('<int:ret_pk>/<int:pk>/update_email/', views.Person_EmailUpdateView.as_view(), name='people_email_update'),
    path('<int:ret_pk>/<int:pk>/update_address/', views.Person_AddressUpdateView.as_view(), name='people_address_update'),
    path('<int:ret_pk>/<int:pk>/update_staff/', views.Person_Legal_Person_NaturalUpdateView.as_view(), name='people_staff_update'),
    path('<int:pk>/delete/', views.PersonDeleteView.as_view(), name='people_delete'),
    path('<int:pk>/delete_natural/', views.Person_NaturalDeleteView.as_view(), name='people_natural_delete'),
    path('<int:pk>/delete_legal/', views.Person_LegalDeleteView.as_view(), name='people_legal_delete'),
    path('<int:ret_pk>/<int:pk>/delete_phone/', views.Person_PhoneDeleteView.as_view(), name='people_phone_delete'),
    path('<int:ret_pk>/<int:pk>/delete_email/', views.Person_EmailDeleteView.as_view(), name='people_email_delete'),
    path('<int:ret_pk>/<int:pk>/delete_address/', views.Person_AddressDeleteView.as_view(), name='people_address_delete'),
    path('<int:ret_pk>/<int:pk>/delete_staff/', views.Person_Legal_Person_NaturalDeleteView.as_view(), name='people_staff_delete'),
]
