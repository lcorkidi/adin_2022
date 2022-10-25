from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericUpdateView, GenericDeleteView, GenericActivateView
from properties.forms.estate_forms import EstateCreateForm, EstateDetailForm, EstateUpdateForm, EstateDeleteForm, EstateActivateForm, EstateListModelFormSet
from properties.models import Estate
from properties.utils import estate_related_data, GetActionsOn, GetIncludedStates

title = Estate._meta.verbose_name_plural
ref_urls = { 'list':'properties:estate_list', 'create':'properties:estate_create', 'detail':'properties:estate_detail', 'update':'properties:estate_update', 'delete':'properties:estate_delete', 'activate':'properties:estate_activate' }

class EstateListView(GenericListView):

    formset = EstateListModelFormSet
    model = Estate
    choice_fields = ['address']
    title = title
    ref_urls = ref_urls
    actions_on = GetActionsOn
    list_order = 'national_number'
    permission_required = 'properties.view_estate'
    include_states = GetIncludedStates

class EstateCreateView(GenericCreateView):

    template = 'adin/generic_create.html'
    form = EstateCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    permission_required = 'properties.add_estate'

class EstateDetailView(GenericDetailView):

    title = title
    model = Estate
    form = EstateDetailForm
    ref_urls = ref_urls
    choice_fields = ['type']
    fk_fields = ['address', 'person']
    related_data = estate_related_data
    actions_on = GetActionsOn
    permission_required = 'properties.view_estate'

class EstateUpdateView(GenericUpdateView):

    model = Estate
    form = EstateUpdateForm
    title = title
    ref_urls = ref_urls
    readonly_fields = ['national_number']
    choice_fields = ['type']
    fk_fields = ['address', 'person']
    actions_on = GetActionsOn
    related_data = estate_related_data
    permission_required = 'properties.change_estate'

class EstateDeleteView(GenericDeleteView):

    title = title
    model = Estate
    form = EstateDeleteForm
    ref_urls = ref_urls
    choice_fields = ['type']
    fk_fields = ['address', 'person']
    related_data = estate_related_data
    actions_on = GetActionsOn
    permission_required = 'properties.delete_estate'

class EstateActivateView(GenericActivateView):

    title = title
    model = Estate
    form = EstateActivateForm
    ref_urls = ref_urls
    choice_fields = ['type']
    fk_fields = ['address', 'person']
    related_data = estate_related_data
    actions_on = GetActionsOn
    permission_required = 'properties.activate_estate'
