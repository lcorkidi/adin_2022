from django.urls import path

from accounting.views.account_views import AccountListView, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'accounting'

urlpatterns = [
    path('account_list', AccountListView.as_view(), name='account_list'),
    path('account_create/', AccountCreateView.as_view(), name='account_create'),
    path('<int:pk>/account_detail/',AccountDetailView.as_view(),name='account_detail'),
    path('<int:pk>/account_update/', AccountUpdateView.as_view(), name='account_update'),
    path('<int:pk>/account_delete/', AccountDeleteView.as_view(), name='account_delete'),
]
