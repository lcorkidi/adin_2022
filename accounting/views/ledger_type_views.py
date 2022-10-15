from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView, GenericActivateView
from accounting.models import Ledger_Type
from accounting.forms.ledger_type_forms import Ledger_TypeDetailModelForm, Ledger_TypeCreateModelForm, Ledger_TypeDeleteModelForm, Ledger_TypeActivateModelForm, Ledger_TypeListModelFormSet
from accounting.utils import GetIncludedStates, GetActionsOn

title = Ledger_Type._meta.verbose_name_plural
ref_urls = { 'list':'accounting:ledger_type_list', 'create':'accounting:ledger_type_create', 'detail':'accounting:ledger_type_detail', 'delete':'accounting:ledger_type_delete', 'activate':'accounting:ledger_type_activate' }

class Ledger_TypeListView(GenericListView):

    formset = Ledger_TypeListModelFormSet
    model = Ledger_Type
    title = title
    ref_urls = ref_urls
    actions_on = GetActionsOn
    list_order = 'name'
    permission_required = 'accounting.view_ledger_type'
    include_states = GetIncludedStates

class Ledger_TypeCreateView(GenericCreateView):

    form = Ledger_TypeCreateModelForm
    title = title
    ref_urls = ref_urls
    permission_required = 'accounting.add_ledger_type'

class Ledger_TypeDetailView(GenericDetailView):

    title = title
    model = Ledger_Type
    form = Ledger_TypeDetailModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'accounting.view_ledger_type'

class Ledger_TypeDeleteView(GenericDeleteView):

    title = title
    model = Ledger_Type
    form = Ledger_TypeDeleteModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'accounting.delete_ledger_type'

class Ledger_TypeActivateView(GenericActivateView):

    title = title
    model = Ledger_Type
    form = Ledger_TypeActivateModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'accounting.activate_ledger'
