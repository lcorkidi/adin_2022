from adin.core.views import GenericCreateRelatedView, GenericUpdateRelatedView, GenericDeleteRelatedView, GenericActivateRelatedView
from people.models import Person_E_Mail
from people.forms.person_e_mail_forms import Person_E_MailCreateForm, Person_E_MailUpdateForm, Person_E_MailDeleteForm, Person_E_MailActivateForm

title = Person_E_Mail._meta.verbose_name_plural
ref_urls = { 'list':'people:person_list', 'create':'people:person_create', 'detail':'people:person_detail', 'update':'people:person_update', 'delete':'people:person_delete' }
rel_urls = { 'create': 'people:person_e_mail_create', 'delete': 'people:person_e_mail_delete', 'update': 'people:person_e_mail_update' }

class Person_EmailCreateView(GenericCreateRelatedView):

    form = Person_E_MailCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['person']
    fk_fields = ['person']
    permission_required = 'people.add_person_e_mail'
    related_fields = ['person', 'e_mail']

class Person_EmailUpdateView(GenericUpdateRelatedView):

    model = Person_E_Mail
    form = Person_E_MailUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['person', 'e_mail']
    fk_fields = ['person']
    permission_required = 'people.change_person_e_mail'

class Person_EmailDeleteView(GenericDeleteRelatedView):

    model = Person_E_Mail
    form = Person_E_MailDeleteForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['use']
    fk_fields = ['person']
    permission_required = 'people.delete_person_e_mail'

class Person_EmailActivateView(GenericActivateRelatedView):

    model = Person_E_Mail
    form = Person_E_MailActivateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['use']
    fk_fields = ['person']
    permission_required = 'people.activate_person'
