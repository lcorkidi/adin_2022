from django.urls import path

from accounting.views.account_views import AccountListView, AccountListSomeView, AccountListAllView, AccountCreateView, AccountDetailView, AccountUpdateView, AccountUpdateSomeView, AccountUpdateAllView, AccountDeleteView, AccountActivateView

app_name = 'accounting'

urlpatterns = [
    path('account_list', AccountListView.as_view(), name='account_list'),
    path('account_list_some', AccountListSomeView.as_view(), name='account_list_some'),
    path('account_list_all', AccountListAllView.as_view(), name='account_list_all'),
    path('account_create/', AccountCreateView.as_view(), name='account_create'),
    path('<int:pk>/account_detail/',AccountDetailView.as_view(),name='account_detail'),
    path('<int:pk>/account_update/', AccountUpdateView.as_view(), name='account_update'),
    path('<int:pk>/account_update_some/', AccountUpdateSomeView.as_view(), name='account_update_some'),
    path('<int:pk>/account_update_all/', AccountUpdateAllView.as_view(), name='account_update_all'),
    path('<int:pk>/account_delete/', AccountDeleteView.as_view(), name='account_delete'),
    path('<int:pk>/account_activate/', AccountActivateView.as_view(), name='account_activate'),
]
