from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('', views.PeopleListView.as_view(), name='people_list'),
    path('create/', views.PeopleCreateView.as_view(), name='people_create'),
    path('create_natural/', views.People_NaturalCreateView.as_view(), name='people_natural_create'),
    path('create_legal/', views.People_LegalCreateView.as_view(), name='people_legal_create'),
    path('<int:pk>/create_phone/', views.People_PhoneCreateView.as_view(), name='people_phone_create'),
    path('<int:pk>/create_email/', views.People_EmailCreateView.as_view(), name='people_email_create'),
    path('<int:pk>/create_address/', views.People_AddressCreateView.as_view(), name='people_address_create'),
    path('<int:pk>/detail/',views.PeopleDetailView.as_view(),name='people_detail'),
    path('<int:pk>/update/', views.PeopleUpdateView.as_view(), name='people_update'),
    path('<int:pk>/update_natural/', views.People_NaturalUpdateView.as_view(), name='people_natural_update'),
    path('<int:pk>/update_legal/', views.People_LegalUpdateView.as_view(), name='people_legal_update'),
    path('<int:pk>/delete/', views.PeopleDeleteView.as_view(), name='people_delete'),
    path('<int:pk>/delete_phone/', views.People_PhoneDeleteView.as_view(), name='people_phone_delete'),
    path('<int:pk>/delete_email/', views.People_EmailDeleteView.as_view(), name='people_email_delete'),
    path('<int:pk>/delete_address/', views.People_AddressDeleteView.as_view(), name='people_address_delete'),
]
