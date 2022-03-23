from adin.core.views import GenericCreateRelatedView, GenericUpdateRelatedView, GenericDeleteRelatedView
from properties.models import Estate_Person
from properties.forms.estate_person_forms import Estate_PersonCreateForm, Estate_PersonUpdateForm

title = Estate_Person._meta.verbose_name_plural
ref_urls = { 'list':'properties:estate_list', 'create':'properties:estate_create', 'detail':'properties:estate_detail', 'update':'properties:estate_update', 'delete':'properties:estate_delete' }
rel_urls = { 'create': 'properties:estate_person_create', 'delete': 'properties:estate_person_delete', 'update': 'properties:estate_person_update' }

class Estate_PersonCreateView(GenericCreateRelatedView):

    form = Estate_PersonCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['estate']
    fk_fields = ['estate']
    permission_required = 'properties.add_estate_person'
    related_fields = ['estate', 'person']

class Estate_PersonUpdateView(GenericUpdateRelatedView):

    model = Estate_Person
    form = Estate_PersonUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['estate', 'person']
    fk_fields = ['estate', 'person']
    permission_required = 'properties.change_estate_person'

class Estate_PersonDeleteView(GenericDeleteRelatedView):

    model = Estate_Person
    form = Estate_PersonUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    fk_fields = ['estate', 'person']
    permission_required = 'properties.delete_estate_person'
