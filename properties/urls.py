from django.urls import path
from properties.views.estate_views import EstateListView, EstateDetailView, EstateCreateView, EstateUpdateView, EstateDeleteView

app_name = 'properties'

urlpatterns = [
    path('estate_list', EstateListView.as_view(), name='estate_list'), 
    path('estate_create/', EstateCreateView.as_view(), name='estate_create'),
    path('<str:pk>/estate_detail/', EstateDetailView.as_view(),name='estate_detail'),
    path('<str:pk>/estate_update/', EstateUpdateView.as_view(), name='estate_update'),
    path('<str:pk>/estate_delete/', EstateDeleteView.as_view(), name='estate_delete'),
]
