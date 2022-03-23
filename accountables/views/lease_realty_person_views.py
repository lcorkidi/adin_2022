from adin.core.views import GenericCreateRelatedView, GenericUpdateRelatedView, GenericDeleteRelatedView
from accountables.models import Lease_Realty_Person
from accountables.forms.lease_realty_person_forms import Lease_Realty_PersonCreateForm, Lease_Realty_PersonUpdateForm

title = Lease_Realty_Person._meta.verbose_name_plural
ref_urls = { 'list':'accountables:lease_realty_list', 'create':'accountables:lease_realty_create', 'detail':'accountables:lease_realty_detail', 'update':'accountables:lease_realty_update', 'delete':'accountables:lease_realty_delete' }
rel_urls = { 'create': 'accountables:lease_realty_person_create', 'delete': 'accountables:lease_realty_person_delete', 'update': 'accountables:lease_realty_person_update' }

class Lease_Realty_PersonCreateView(GenericCreateRelatedView):

    form = Lease_Realty_PersonCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['lease']
    fk_fields = ['lease']
    permission_required = 'accountables.add_lease_realty_person'
    related_fields = ['lease', 'person']

class Lease_Realty_PersonUpdateView(GenericUpdateRelatedView):

    model = Lease_Realty_Person
    form = Lease_Realty_PersonUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['lease', 'person']
    fk_fields = ['lease', 'person']
    permission_required = 'accountables.change_lease_realty_person'

class Lease_Realty_PersonDeleteView(GenericDeleteRelatedView):

    model = Lease_Realty_Person
    form = Lease_Realty_PersonUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    choice_fields = ['role']
    fk_fields = ['lease', 'person']
    permission_required = 'accountables.delete_lease_realty_person'
