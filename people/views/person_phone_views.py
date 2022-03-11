from adin.core.views import GenericCreateRelatedView, GenericUpdateRelatedView, GenericDeleteRelatedView
from people.models import Person_Phone
from people.forms.person_phone_forms import Person_PhoneCreateForm, Person_PhoneUpdateForm

ref_urls = { 'list':'people:person_list', 'create':'people:person_create', 'detail':'people:person_detail', 'update':'people:person_update', 'delete':'people:person_delete' }
rel_urls = { 'create': 'people:person_phone_create', 'delete': 'people:person_phone_delete', 'update': 'people:person_phone_update' }

class Person_PhoneCreateView(GenericCreateRelatedView):

    template = 'people/people_related_create.html'
    form = Person_PhoneCreateForm
    title = Person_Phone._meta.verbose_name_plural
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['person']
    fk_fields = ['person']
    permission_required = 'people.add_person_phone'

class Person_PhoneUpdateView(GenericUpdateRelatedView):

    template = 'people/people_related_update.html'
    model = Person_Phone
    form = Person_PhoneUpdateForm
    title = Person_Phone._meta.verbose_name_plural
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['person', 'phone']
    fk_fields = ['person']
    permission_required = 'people.change_person_phone'

class Person_PhoneDeleteView(GenericDeleteRelatedView):

    template = 'people/people_related_delete.html'
    model = Person_Phone
    form = Person_PhoneUpdateForm
    title = Person_Phone._meta.verbose_name_plural
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['use']
    fk_fields = ['person']
    permission_required = 'people.delete_person_phone'
