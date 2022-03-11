from adin.core.views import GenericCreateRelatedView, GenericUpdateRelatedView, GenericDeleteRelatedView
from properties.models import Estate_Person
from properties.forms.estate_person_forms import Estate_PersonCreateForm, Estate_PersonUpdateForm

title = Estate_Person._meta.verbose_name_plural
ref_urls = { 'list':'people:person_list', 'create':'people:person_create', 'detail':'people:person_detail', 'update':'people:person_update', 'delete':'people:person_delete' }
rel_urls = { 'create': 'people:person_phone_create', 'delete': 'people:person_phone_delete', 'update': 'people:person_phone_update' }

class Estate_PersonCreateView(GenericCreateRelatedView):

    template = 'people/people_related_create.html'
    form = Estate_PersonCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['person']
    fk_fields = ['person']
    permission_required = 'people.add_person_phone'

class Estate_PersonUpdateView(GenericUpdateRelatedView):

    template = 'people/people_related_update.html'
    model = Estate_Person
    form = Estate_PersonUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['person', 'phone']
    fk_fields = ['person']
    permission_required = 'people.change_person_phone'

class Estate_PersonDeleteView(GenericDeleteRelatedView):

    template = 'people/people_related_delete.html'
    model = Estate_Person
    form = Estate_PersonUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['use']
    fk_fields = ['person']
    permission_required = 'people.delete_person_phone'
