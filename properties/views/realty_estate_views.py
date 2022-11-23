from adin.core.views import GenericCreateRelatedView, GenericUpdateRelatedView, GenericDeleteRelatedView, GenericActivateRelatedView
from properties.models import Realty_Estate
from properties.forms.realty_estate_forms import Realty_EstateCreateForm, Realty_EstateUpdateForm, Realty_EstateDeleteForm, Realty_EstateActivateForm

title = Realty_Estate._meta.verbose_name_plural
ref_urls = { 'list':'properties:realty_list', 'create':'properties:realty_create', 'detail':'properties:realty_detail', 'update':'properties:realty_update', 'delete':'properties:realty_delete' }
rel_urls = { 'create': 'properties:realty_estate_create', 'delete': 'properties:realty_estate_delete', 'update': 'properties:realty_estate_update' }

class Realty_EstateCreateView(GenericCreateRelatedView):

    form = Realty_EstateCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['realty']
    fk_fields = ['realty']
    permission_required = 'properties.add_realty_estate'
    related_fields = ['realty', 'estate']

class Realty_EstateUpdateView(GenericUpdateRelatedView):

    model = Realty_Estate
    form = Realty_EstateUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['realty', 'estate']
    fk_fields = ['realty', 'estate']
    permission_required = 'properties.change_realty_estate'

class Realty_EstateDeleteView(GenericDeleteRelatedView):

    model = Realty_Estate
    form = Realty_EstateDeleteForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    fk_fields = ['realty', 'estate']
    actions_on = ['update']
    permission_required = 'properties.delete_realty_estate'

class Realty_EstateActivateView(GenericActivateRelatedView):

    model = Realty_Estate
    form = Realty_EstateActivateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    fk_fields = ['realty', 'estate']
    permission_required = 'properties.activate_realty'
