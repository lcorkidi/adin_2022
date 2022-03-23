from django.urls import path

from home.views.user_views import UserLogInView, UserLogOutView, UserCreationView, UserPasswordChangeView
from home.views.home_views import HomeView

app_name = 'home'
urlpatterns = [
    path('', UserLogInView.as_view(), name='user_login'),
    path('logout/', UserLogOutView.as_view(), name='user_logout'),
    path('register/', UserCreationView.as_view(), name='user_register'),
    path('password_change/', UserPasswordChangeView.as_view(), name='user_password_change'),
    path('home/', HomeView.as_view(), name='user_home'),
]