from adin.core.views import GenericCreateRelatedView, GenericUpdateRelatedView, GenericDeleteRelatedView, GenericActivateRelatedView
from accountables.models import Date_Value
from accountables.forms.date_value_forms import Date_ValueCreateForm, Date_ValueUpdateForm

title = Date_Value._meta.verbose_name_plural
ref_urls = { 'list':'accountables:lease_realty_list', 'create':'accountables:lease_realty_create', 'detail':'accountables:lease_realty_detail', 'update':'accountables:lease_realty_update', 'delete':'accountables:lease_realty_delete' }
rel_urls = { 'create': 'accountables:date_value_create', 'delete': 'accountables:date_value_delete', 'update': 'accountables:date_value_update' }

class Date_ValueCreateView(GenericCreateRelatedView):

    form = Date_ValueCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['accountable']
    fk_fields = ['accountable']
    permission_required = 'accountables.add_date_value'

class Date_ValueUpdateView(GenericUpdateRelatedView):

    model = Date_Value
    form = Date_ValueUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['accountable', 'date']
    fk_fields = ['accountable']
    permission_required = 'accountables.change_date_value'

class Date_ValueDeleteView(GenericDeleteRelatedView):

    model = Date_Value
    form = Date_ValueUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    fk_fields = ['accountable']
    permission_required = 'accountables.delete_date_value'

class Date_ValueActivateView(GenericActivateRelatedView):

    model = Date_Value
    form = Date_ValueUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    fk_fields = ['accountable']
    permission_required = 'accountables.activate_lease_realty'
