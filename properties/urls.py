from django.urls import path
from properties.views.estate_views import EstateListView, EstateDetailView, EstateCreateView, EstateUpdateView, EstateDeleteView
from properties.views.estate_person_views import Estate_PersonCreateView, Estate_PersonUpdateView, Estate_PersonDeleteView
from properties.views.estate_appraisals_views import Estate_AppraisalCreateView, Estate_AppraisalUpdateView, Estate_AppraisalDeleteView
from properties.views.realty_views import RealtyListView, RealtyCreateView, RealtyDetailView, RealtyUpdateView, RealtyDeleteView
from properties.views.realty_estate_views import Realty_EstateCreateView, Realty_EstateUpdateView, Realty_EstateDeleteView
app_name = 'properties'

urlpatterns = [
    path('estate_list', EstateListView.as_view(), name='estate_list'), 
    path('estate_create/', EstateCreateView.as_view(), name='estate_create'),
    path('<str:pk>/estate_detail/', EstateDetailView.as_view(),name='estate_detail'),
    path('<str:pk>/estate_update/', EstateUpdateView.as_view(), name='estate_update'),
    path('<str:pk>/estate_delete/', EstateDeleteView.as_view(), name='estate_delete'),
    path('<str:pk>/estate_person_create/', Estate_PersonCreateView.as_view(), name='estate_person_create'),
    path('<str:ret_pk>/<str:pk>/estate_person_update/', Estate_PersonUpdateView.as_view(), name='estate_person_update'),
    path('<str:ret_pk>/<str:pk>/estate_person_delete/', Estate_PersonDeleteView.as_view(), name='estate_person_delete'),
    path('<str:pk>/estate_appraisal_create/', Estate_AppraisalCreateView.as_view(), name='estate_appraisal_create'),
    path('<str:ret_pk>/<str:pk>/estate_appraisal_update/', Estate_AppraisalUpdateView.as_view(), name='estate_appraisal_update'),
    path('<str:ret_pk>/<str:pk>/estate_appraisal_delete/', Estate_AppraisalDeleteView.as_view(), name='estate_appraisal_delete'),
    path('realty_list', RealtyListView.as_view(), name='realty_list'), 
    path('realty_create/', RealtyCreateView.as_view(), name='realty_create'),
    path('<str:pk>/realty_detail/', RealtyDetailView.as_view(),name='realty_detail'),
    path('<str:pk>/realty_update/', RealtyUpdateView.as_view(), name='realty_update'),
    path('<str:pk>/realty_delete/', RealtyDeleteView.as_view(), name='realty_delete'),
    path('<str:pk>/realty_estate_create/', Realty_EstateCreateView.as_view(), name='realty_estate_create'),
    path('<str:ret_pk>/<str:pk>realty_/estate_update/', Realty_EstateUpdateView.as_view(), name='realty_estate_update'),
    path('<str:ret_pk>/<str:pk>/realty_estate_delete/', Realty_EstateDeleteView.as_view(), name='realty_estate_delete'),
]
