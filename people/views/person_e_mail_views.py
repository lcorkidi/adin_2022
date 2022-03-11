from adin.core.views import GenericCreateRelatedView, GenericUpdateRelatedView, GenericDeleteRelatedView
from people.models import Person_E_Mail
from people.forms.person_e_mail_forms import Person_EmailCreateForm, Person_EmailUpdateForm

ref_urls = { 'list':'people:person_list', 'create':'people:person_create', 'detail':'people:person_detail', 'update':'people:person_update', 'delete':'people:person_delete' }
rel_urls = { 'create': 'people:person_e_mail_create', 'delete': 'people:person_e_mail_delete', 'update': 'people:person_e_mail_update' }

class Person_EmailCreateView(GenericCreateRelatedView):

    template = 'people/people_related_create.html'
    form = Person_EmailCreateForm
    title = Person_E_Mail._meta.verbose_name_plural
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['person']
    fk_fields = ['person']
    permission_required = 'people.add_person_e_mail'

class Person_EmailUpdateView(GenericUpdateRelatedView):

    template = 'people/people_related_update.html'
    model = Person_E_Mail
    form = Person_EmailUpdateForm
    title = Person_E_Mail._meta.verbose_name_plural
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['person', 'e_mail']
    fk_fields = ['person']
    permission_required = 'people.change_person_e_mail'

class Person_EmailDeleteView(GenericDeleteRelatedView):

    template = 'people/people_related_delete.html'
    model = Person_E_Mail
    form = Person_EmailUpdateForm
    title = Person_E_Mail._meta.verbose_name_plural
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['use']
    fk_fields = ['person']
    permission_required = 'people.delete_person_e_mail'
