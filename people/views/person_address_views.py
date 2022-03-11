from adin.core.views import GenericCreateRelatedView, GenericUpdateRelatedView, GenericDeleteRelatedView
from people.models import Person_Address
from people.forms.person_address_forms import Person_AddressCreateForm, Person_AddressUpdateForm

ref_urls = { 'list':'people:person_list', 'create':'people:person_create', 'detail':'people:person_detail', 'update':'people:person_update', 'delete':'people:person_delete' }
rel_urls = { 'create': 'people:person_address_create', 'delete': 'people:person_address_delete', 'update': 'people:person_address_update' }

class Person_AddressCreateView(GenericCreateRelatedView):

    template = 'people/people_related_create.html'
    form = Person_AddressCreateForm
    title = Person_Address._meta.verbose_name_plural
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['person']
    fk_fields = ['person']

class Person_AddressUpdateView(GenericUpdateRelatedView):

    template = 'people/people_related_update.html'
    model = Person_Address
    form = Person_AddressUpdateForm
    title = Person_Address._meta.verbose_name_plural
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['person', 'address']
    fk_fields = ['person', 'address']

class Person_AddressDeleteView(GenericDeleteRelatedView):

    template = 'people/people_related_delete.html'
    model = Person_Address
    form = Person_AddressUpdateForm
    title = Person_Address._meta.verbose_name_plural
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['use']
    fk_fields = ['person', 'address']
