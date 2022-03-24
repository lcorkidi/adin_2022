from django.urls import path

from properties.views.estate_views import EstateListView, EstateListSomeView, EstateListAllView, EstateDetailView, EstateCreateView, EstateUpdateView, EstateUpdateSomeView, EstateUpdateAllView, EstateDeleteView, EstateActivateView
from properties.views.estate_person_views import Estate_PersonCreateView, Estate_PersonUpdateView, Estate_PersonDeleteView, Estate_PersonActivateView
from properties.views.estate_appraisals_views import Estate_AppraisalCreateView, Estate_AppraisalUpdateView, Estate_AppraisalDeleteView, Estate_AppraisalActivateView
from properties.views.realty_views import RealtyListView, RealtyListSomeView, RealtyListAllView, RealtyCreateView, RealtyDetailView, RealtyUpdateView, RealtyUpdateSomeView, RealtyUpdateAllView, RealtyDeleteView, RealtyActivateView
from properties.views.realty_estate_views import Realty_EstateCreateView, Realty_EstateUpdateView, Realty_EstateDeleteView, Realty_EstateActivateView

app_name = 'properties'

urlpatterns = [
    path('estate_list', EstateListView.as_view(), name='estate_list'), 
    path('estate_list_some', EstateListSomeView.as_view(), name='estate_list_some'), 
    path('estate_list_all', EstateListAllView.as_view(), name='estate_list_all'), 
    path('estate_create/', EstateCreateView.as_view(), name='estate_create'),
    path('<str:pk>/estate_detail/', EstateDetailView.as_view(),name='estate_detail'),
    path('<str:pk>/estate_update/', EstateUpdateView.as_view(), name='estate_update'),
    path('<str:pk>/estate_update_some/', EstateUpdateSomeView.as_view(), name='estate_update_some'),
    path('<str:pk>/estate_update_all/', EstateUpdateAllView.as_view(), name='estate_update_all'),
    path('<str:pk>/estate_delete/', EstateDeleteView.as_view(), name='estate_delete'),
    path('<str:pk>/estate_activate/', EstateActivateView.as_view(), name='estate_activate'),
    path('<str:pk>/estate_person_create/', Estate_PersonCreateView.as_view(), name='estate_person_create'),
    path('<str:ret_pk>/<str:pk>/estate_person_update/', Estate_PersonUpdateView.as_view(), name='estate_person_update'),
    path('<str:ret_pk>/<str:pk>/estate_person_delete/', Estate_PersonDeleteView.as_view(), name='estate_person_delete'),
    path('<str:ret_pk>/<str:pk>/estate_person_activate/', Estate_PersonActivateView.as_view(), name='estate_person_activate'),
    path('<str:pk>/estate_appraisal_create/', Estate_AppraisalCreateView.as_view(), name='estate_appraisal_create'),
    path('<str:ret_pk>/<str:pk>/estate_appraisal_update/', Estate_AppraisalUpdateView.as_view(), name='estate_appraisal_update'),
    path('<str:ret_pk>/<str:pk>/estate_appraisal_delete/', Estate_AppraisalDeleteView.as_view(), name='estate_appraisal_delete'),
    path('<str:ret_pk>/<str:pk>/estate_appraisal_activate/', Estate_AppraisalActivateView.as_view(), name='estate_appraisal_activate'),
    path('realty_list', RealtyListView.as_view(), name='realty_list'), 
    path('realty_list_some', RealtyListSomeView.as_view(), name='realty_list_some'), 
    path('realty_list_all', RealtyListAllView.as_view(), name='realty_list_all'), 
    path('realty_create/', RealtyCreateView.as_view(), name='realty_create'),
    path('<str:pk>/realty_detail/', RealtyDetailView.as_view(),name='realty_detail'),
    path('<str:pk>/realty_update/', RealtyUpdateView.as_view(), name='realty_update'),
    path('<str:pk>/realty_update_some/', RealtyUpdateSomeView.as_view(), name='realty_update_some'),
    path('<str:pk>/realty_update_all/', RealtyUpdateAllView.as_view(), name='realty_update_all'),
    path('<str:pk>/realty_delete/', RealtyDeleteView.as_view(), name='realty_delete'),
    path('<str:pk>/realty_activate/', RealtyActivateView.as_view(), name='realty_activate'),
    path('<str:pk>/realty_estate_create/', Realty_EstateCreateView.as_view(), name='realty_estate_create'),
    path('<str:ret_pk>/<str:pk>realty_/estate_update/', Realty_EstateUpdateView.as_view(), name='realty_estate_update'),
    path('<str:ret_pk>/<str:pk>/realty_estate_delete/', Realty_EstateDeleteView.as_view(), name='realty_estate_delete'),
    path('<str:ret_pk>/<str:pk>/realty_estate_activate/', Realty_EstateActivateView.as_view(), name='realty_estate_activate'),
]
