from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericUpdateView, GenericDeleteView, GenericActivateView
from properties.forms.realty_forms import RealtyCreateForm, RealtyDetailForm, RealtyUpdateForm, RealtyDeleteForm, RealtyActivateForm, RealtyListModelFormSet
from properties.models import Realty
from properties.utils import realty_related_data, GetIncludedStates, GetActionsOn

title = Realty._meta.verbose_name_plural
ref_urls = { 'list':'properties:realty_list', 'create':'properties:realty_create', 'detail':'properties:realty_detail', 'update':'properties:realty_update', 'delete':'properties:realty_delete', 'activate':'properties:realty_activate' }

class RealtyListView(GenericListView):

    formset = RealtyListModelFormSet
    model = Realty
    choice_fields = ['use']
    title = title
    ref_urls = ref_urls
    actions_on = GetActionsOn
    list_order = 'code'
    permission_required = 'properties.view_realty'
    include_states = GetIncludedStates

class RealtyCreateView(GenericCreateView):

    template = 'adin/generic_create.html'
    form = RealtyCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    permission_required = 'properties.add_realty'

class RealtyDetailView(GenericDetailView):

    title = title
    model = Realty
    form = RealtyDetailForm
    ref_urls = ref_urls
    choice_fields = ['type', 'use']
    fk_fields = ['address', 'estate']
    related_data = realty_related_data
    actions_on = GetActionsOn
    permission_required = 'properties.view_realty'

class RealtyUpdateView(GenericUpdateView):

    model = Realty
    form = RealtyUpdateForm
    title = title
    ref_urls = ref_urls
    readonly_fields = ['code', 'address']
    choice_fields = ['type', 'use']
    fk_fields = ['address', 'estate']
    actions_on = GetActionsOn
    related_data = realty_related_data
    permission_required = 'properties.change_realty'

class RealtyDeleteView(GenericDeleteView):

    title = title
    model = Realty
    form = RealtyDeleteForm
    ref_urls = ref_urls
    choice_fields = ['type', 'use']
    fk_fields = ['address', 'estate']
    related_data = realty_related_data
    actions_on = GetActionsOn
    permission_required = 'properties.delete_realty'

class RealtyActivateView(GenericActivateView):

    title = title
    model = Realty
    form = RealtyActivateForm
    ref_urls = ref_urls
    choice_fields = ['type', 'use']
    fk_fields = ['address', 'estate']
    related_data = realty_related_data
    actions_on = GetActionsOn
    permission_required = 'properties.activate_realty'
