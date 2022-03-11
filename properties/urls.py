from django.urls import path
from properties.views.estate_views import EstatesListView

app_name = 'properties'

urlpatterns = [
    path('estate_list', EstatesListView.as_view(), name='estate_list'),
]
