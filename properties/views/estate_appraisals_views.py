from adin.core.views import GenericCreateRelatedView, GenericUpdateRelatedView, GenericDeleteRelatedView, GenericActivateRelatedView
from properties.models import Estate_Appraisal
from properties.forms.estate_appraisal_forms import Estate_AppraisalCreateForm, Estate_AppraisalUpdateForm

title = Estate_Appraisal._meta.verbose_name_plural
ref_urls = { 'list':'properties:estate_list', 'create':'properties:estate_create', 'detail':'properties:estate_detail', 'update':'properties:estate_update', 'delete':'properties:estate_delete' }
rel_urls = { 'create': 'properties:estate_appraisal_create', 'delete': 'properties:estate_appraisal_delete', 'update': 'properties:estate_appraisal_update' }

class Estate_AppraisalCreateView(GenericCreateRelatedView):

    form = Estate_AppraisalCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['estate']
    fk_fields = ['estate']
    permission_required = 'properties.add_estate_appraisal'
    related_fields = ['estate', 'appraisal']

class Estate_AppraisalUpdateView(GenericUpdateRelatedView):

    model = Estate_Appraisal
    form = Estate_AppraisalUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['estate']
    fk_fields = ['estate']
    permission_required = 'properties.change_estate_appraisal'

class Estate_AppraisalDeleteView(GenericDeleteRelatedView):

    model = Estate_Appraisal
    form = Estate_AppraisalUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['type']
    fk_fields = ['estate']
    permission_required = 'properties.delete_estate_appraisal'

class Estate_AppraisalActivateView(GenericActivateRelatedView):

    model = Estate_Appraisal
    form = Estate_AppraisalUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['type']
    fk_fields = ['estate']
    permission_required = 'properties.activate_estate'
