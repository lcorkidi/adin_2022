from django.urls import path
from properties.views.estate_views import EstateListView, EstateDetailView, EstateCreateView, EstateUpdateView, EstateDeleteView
from properties.views.estate_person_views import Estate_PersonCreateView, Estate_PersonUpdateView, Estate_PersonDeleteView
from properties.views.estate_appraisals_views import Estate_AppraisalCreateView, Estate_AppraisalUpdateView, Estate_AppraisalDeleteView
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
]
