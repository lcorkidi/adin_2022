from django.urls import path

from home.views.user_views import UserLogInView
from home.views.home_views import HomeView

app_name = 'home'
urlpatterns = [
    path('', UserLogInView.as_view(), name='user_login'),
    path('home/', HomeView.as_view(), name='user_home'),
]