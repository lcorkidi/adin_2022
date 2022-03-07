from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('', views.PeopleListView.as_view(), name='people_list'),
    # path('create/', views.PeopleCreateView.as_view(), name='people_create'),
    # path('<int:pk>/detail/',views.PeopleDetailView.as_view(),name='people_detail'),
    # path('<int:pk>/update/', views.PeopleUpdateView.as_view(), name='people_update'),
    # path('<int:pk>/delete/', views.PeopleDeleteView.as_view(), name='people_delete'),
]
