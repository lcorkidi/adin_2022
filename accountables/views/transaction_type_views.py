from adin.core.views import GenericListView, GenericCreateView, GenericDetailView, GenericDeleteView, GenericActivateView
from accountables.forms.transaction_type_forms import Transaction_TypeDetailModelForm, Transaction_TypeCreateModelForm, Transaction_TypeDeleteModelForm, Transaction_TypeActivateModelForm, Transaction_TypeListModelFormSet
from accountables.models import Transaction_Type
from accountables.utils import GetActionsOn, GetIncludedStates

title = Transaction_Type._meta.verbose_name_plural
ref_urls = { 'list':'accountables:transaction_type_list', 'create':'accountables:transaction_type_create', 'detail':'accountables:transaction_type_detail', 'delete':'accountables:transaction_type_delete', 'activate':'accountables:transaction_type_activate'}
        
class Transaction_TypeListView(GenericListView):

    formset = Transaction_TypeListModelFormSet
    model = Transaction_Type
    title = title
    ref_urls = ref_urls
    actions_on = GetActionsOn
    list_order = 'name'
    permission_required = 'references.view_transaction_type'
    include_states = GetIncludedStates

class Transaction_TypeCreateView(GenericCreateView):

    form = Transaction_TypeCreateModelForm
    title = title
    ref_urls = ref_urls
    permission_required = 'accountables.add_transaction_type'

class Transaction_TypeDetailView(GenericDetailView):

    title = title
    model = Transaction_Type
    form = Transaction_TypeDetailModelForm
    ref_urls = ref_urls
    actions_on = GetActionsOn
    permission_required = 'accountables.view_transaction_type'

class Transaction_TypeDeleteView(GenericDeleteView):

    title = title
    model = Transaction_Type
    form = Transaction_TypeDeleteModelForm
    ref_urls = ref_urls
    actions_on = GetActionsOn
    permission_required = 'accountables.delete_transaction_type'

class Transaction_TypeActivateView(GenericActivateView):

    title = title
    model = Transaction_Type
    form = Transaction_TypeActivateModelForm
    ref_urls = ref_urls
    actions_on = GetActionsOn
    permission_required = 'accountables.activate_transaction_type'
    success_url = 'list'
