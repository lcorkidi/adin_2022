from pyexpat import model
from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericUpdateView, GenericDeleteView
from properties.forms.estate_forms import EstateCreateForm, EstateDetailForm, EstateUpdateForm, EstateDeleteForm, EstateListModelFormSet
from properties.models import Estate
from properties.utils import estate_m2m_data

title = Estate._meta.verbose_name_plural
ref_urls = { 'list':'properties:estate_list', 'create':'properties:estate_create', 'detail':'properties:estate_detail', 'update':'properties:estate_update', 'delete':'properties:estate_delete' }

class EstateListView(GenericListView):

    template = 'adin/generic_list.html'
    formset = EstateListModelFormSet
    model = Estate
    choice_fields = ['id_type']
    title = title
    ref_urls = ref_urls
    list_order = 'code'

class EstateCreateView(GenericCreateView):

    template = 'adin/generic_create.html'
    form = EstateCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['type', 'id_type']
    choice_fields = ['type', 'id_type']

class EstateDetailView(GenericDetailView):

    title = title
    model = Estate
    form = EstateDetailForm
    ref_urls = ref_urls
    choice_fields = ['type', 'id_type', 'use']
    m2m_data = estate_m2m_data

class EstateUpdateView(GenericUpdateView):

    model = Estate
    form = EstateUpdateForm
    title = title
    ref_urls = ref_urls
    readonly_fields = ['type', 'id_type', 'id_number']
    choice_fields = ['type', 'id_type', 'use']
    m2m_data = estate_m2m_data

class EstateDeleteView(GenericDeleteView):

    title = title
    model = Estate
    form = EstateDeleteForm
    ref_urls = ref_urls
    choice_fields = ['type', 'id_type', 'use']
    m2m_data = estate_m2m_data
