from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.LogInView.as_view(), name='homepage'),
]