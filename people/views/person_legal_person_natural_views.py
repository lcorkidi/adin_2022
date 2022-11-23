from adin.core.views import GenericCreateRelatedView, GenericUpdateRelatedView, GenericDeleteRelatedView, GenericActivateRelatedView
from people.models import Person_Legal_Person_Natural
from people.forms.person_legal_person_natural_forms import Person_Legal_Person_NaturalCreateForm, Person_Legal_Person_NaturalUpdateForm, Person_Legal_Person_NaturalDeleteForm, Person_Legal_Person_NaturalActivateForm

title = Person_Legal_Person_Natural._meta.verbose_name_plural
ref_urls = { 'list':'people:person_list', 'create':'people:person_create', 'detail':'people:person_detail', 'update':'people:person_update', 'delete':'people:person_delete' }
rel_urls = { 'create': 'people:person_legal_person_natural_create', 'delete': 'people:person_legal_person_natural_delete', 'update': 'people:person_legal_person_natural_update' }

class Person_Legal_Person_NaturalCreateView(GenericCreateRelatedView):

    form = Person_Legal_Person_NaturalCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['person_legal']
    fk_fields = [ 'person_legal' ]
    permission_required = 'people.add_person_legal_person_natural'
    related_fields = ['person_legal', 'person_natural']

class Person_Legal_Person_NaturalUpdateView(GenericUpdateRelatedView):

    model = Person_Legal_Person_Natural
    form = Person_Legal_Person_NaturalUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['person_legal', 'person_natural']
    fk_fields = [ 'person_legal', 'person_natural' ]
    permission_required = 'people.change_person_legal_person_natural'

class Person_Legal_Person_NaturalDeleteView(GenericDeleteRelatedView):

    model = Person_Legal_Person_Natural
    form = Person_Legal_Person_NaturalDeleteForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['appointment']
    fk_fields = [ 'person_legal', 'person_natural' ]
    actions_on = ['update']
    permission_required = 'people.delete_person_legal_person_natural'

class Person_Legal_Person_NaturalActivateView(GenericActivateRelatedView):

    model = Person_Legal_Person_Natural
    form = Person_Legal_Person_NaturalActivateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['appointment']
    fk_fields = [ 'person_legal', 'person_natural' ]
    permission_required = 'people.activate_person'
