from adin.core.views import GenericCreateRelatedView, GenericUpdateRelatedView, GenericDeleteRelatedView, GenericActivateRelatedView
from people.models import Person_Address
from people.forms.person_address_forms import Person_AddressCreateForm, Person_AddressUpdateForm, Person_AddressDeleteForm, Person_AddressActivateForm

title = Person_Address._meta.verbose_name_plural
ref_urls = { 'list':'people:person_list', 'create':'people:person_create', 'detail':'people:person_detail', 'update':'people:person_update', 'delete':'people:person_delete' }
rel_urls = { 'create': 'people:person_address_create', 'delete': 'people:person_address_delete', 'update': 'people:person_address_update' }

class Person_AddressCreateView(GenericCreateRelatedView):

    form = Person_AddressCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['person']
    fk_fields = ['person']
    permission_required = 'people.add_person_address'
    related_fields = ['person', 'address']

class Person_AddressUpdateView(GenericUpdateRelatedView):

    model = Person_Address
    form = Person_AddressUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['person', 'address']
    fk_fields = ['person', 'address']
    permission_required = 'people.change_person_address'

class Person_AddressDeleteView(GenericDeleteRelatedView):

    model = Person_Address
    form = Person_AddressDeleteForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['use']
    fk_fields = ['person', 'address']
    actions_on = ['update']
    permission_required = 'people.delete_person_address'

class Person_AddressActivateView(GenericActivateRelatedView):

    model = Person_Address
    form = Person_AddressActivateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['use']
    fk_fields = ['person', 'address']
    permission_required = 'people.activate_person'
