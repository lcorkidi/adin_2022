from adin.core.views import GenericCreateRelatedView, GenericDetailRelatedlView, GenericUpdateRelatedView, GenericDeleteRelatedView, GenericActivateRelatedView
from accountables.models import Accountable_Transaction_Type
from accountables.forms.accountable_transaction_type_forms import Accountable_Transaction_TypeCreateForm, Accountable_Transaction_TypeDetailForm, Accountable_Transaction_TypeUpdateForm, Accountable_Transaction_TypeDeleteForm, Accountable_Transaction_TypeActivateForm


title = Accountable_Transaction_Type._meta.verbose_name_plural
ref_urls = {  'list':'accountables:lease_realty_list', 'create':'accountables:lease_realty_create', 'detail':'accountables:lease_realty_detail', 'update':'accountables:lease_realty_accounting', 'delete':'accountables:lease_realty_delete', 'activate':'accountables:lease_realty_activate', 'accounting':'accountables:lease_realty_accounting' }
rel_urls = { 'create': 'accountables:accountable_transaction_type_create', 'delete': 'accountables:accountable_transaction_type_delete', 'update': 'accountables:accountable_transaction_type_update' }

class Accountable_Transaction_TypeCreateView(GenericCreateRelatedView):

    form = Accountable_Transaction_TypeCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['accountable']
    fk_fields = ['accountable']
    permission_required = 'accountables.add_transaction_type'
    related_fields = ['accountable', 'transaction_type', 'ledger_template']

class Accountable_Transaction_TypeDetailView(GenericDetailRelatedlView):

    model = Accountable_Transaction_Type
    title = title
    form = Accountable_Transaction_TypeDetailForm
    ref_urls = ref_urls
    rel_urls = rel_urls
    fk_fields = [ 'accountalbe', 'transaction_type', 'commit_template', 'bill_template', 'receive_template']
    permission_required = 'accountables.view_accountable_transaction_type'

class Accountable_Transaction_TypeUpdateView(GenericUpdateRelatedView):

    model = Accountable_Transaction_Type
    form = Accountable_Transaction_TypeUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = [ 'accountalbe', 'transaction_type' ]
    fk_fields = [ 'accountalbe', 'transaction_type' ]
    permission_required = 'accountables.change_accountable_transaction_type'

class Accountable_Transaction_TypeDeleteiew(GenericDeleteRelatedView):

    model = Accountable_Transaction_Type
    title = title
    form = Accountable_Transaction_TypeDeleteForm
    ref_urls = ref_urls
    rel_urls = rel_urls
    fk_fields = [ 'accountalbe', 'transaction_type', 'commit_template', 'bill_template', 'receive_template']
    accounting = True
    permission_required = 'accountables.delete_accountable_transaction_type'

class Accountable_Transaction_TypeActivateView(GenericActivateRelatedView):

    model = Accountable_Transaction_Type
    title = title
    form = Accountable_Transaction_TypeActivateForm
    ref_urls = ref_urls
    rel_urls = rel_urls
    fk_fields = [ 'accountalbe', 'transaction_type', 'commit_template', 'bill_template', 'receive_template']
    accounting = True
    permission_required = 'accountables.activate_accountable_transaction_type'
