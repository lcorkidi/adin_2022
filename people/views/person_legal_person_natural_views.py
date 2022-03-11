from adin.core.views import GenericCreateRelatedView, GenericUpdateRelatedView, GenericDeleteRelatedView
from people.models import Person_Legal_Person_Natural
from people.forms.person_legal_person_natural_forms import Person_Legal_Person_NaturalCreateForm, Person_Legal_Person_NaturalUpdateForm

ref_urls = { 'list':'people:person_list', 'create':'people:person_create', 'detail':'people:person_detail', 'update':'people:person_update', 'delete':'people:person_delete' }
rel_urls = { 'create': 'people:person_legal_person_natural_create', 'delete': 'people:person_legal_person_natural_delete', 'update': 'people:person_legal_person_natural_update' }

class Person_Legal_Person_NaturalCreateView(GenericCreateRelatedView):

    template = 'people/people_related_create.html'
    form = Person_Legal_Person_NaturalCreateForm
    title = Person_Legal_Person_Natural._meta.verbose_name_plural
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['person']

class Person_Legal_Person_NaturalUpdateView(GenericUpdateRelatedView):

    template = 'people/people_related_update.html'
    model = Person_Legal_Person_Natural
    form = Person_Legal_Person_NaturalUpdateForm
    title = Person_Legal_Person_Natural._meta.verbose_name_plural
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['person_legal', 'person_naural']

class Person_Legal_Person_NaturalDeleteView(GenericDeleteRelatedView):

    template = 'people/people_related_delete.html'
    model = Person_Legal_Person_Natural
    form = Person_Legal_Person_NaturalUpdateForm
    title = Person_Legal_Person_Natural._meta.verbose_name_plural
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['appointment']
