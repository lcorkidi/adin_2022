from django.urls import path
from properties.views.estate_views import EstateListView, EstateDetailView, EstateCreateView, EstateUpdateView, EstateDeleteView
from properties.views.estate_person_views import Estate_PersonCreateView, Estate_PersonUpdateView, Estate_PersonDeleteView
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
]
