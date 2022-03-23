from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericUpdateView, GenericDeleteView
from properties.forms.realty_forms import RealtyCreateForm, RealtyDetailForm, RealtyUpdateForm, RealtyDeleteForm, RealtyListModelFormSet
from properties.models import Realty
from properties.utils import realty_related_data

title = Realty._meta.verbose_name_plural
ref_urls = { 'list':'properties:realty_list', 'create':'properties:realty_create', 'detail':'properties:realty_detail', 'update':'properties:realty_update', 'delete':'properties:realty_delete' }

class RealtyListView(GenericListView):

    template = 'adin/generic_list.html'
    formset = RealtyListModelFormSet
    model = Realty
    choice_fields = ['use']
    title = title
    ref_urls = ref_urls
    list_order = 'code'
    permission_required = 'properties.view_realty'

class RealtyCreateView(GenericCreateView):

    template = 'adin/generic_create.html'
    form = RealtyCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    permission_required = 'properties.add_realty'

class RealtyDetailView(GenericDetailView):

    title = title
    model = Realty
    form = RealtyDetailForm
    ref_urls = ref_urls
    choice_fields = ['type', 'use']
    fk_fields = ['address', 'estate']
    related_data = realty_related_data
    permission_required = 'properties.view_realty'

class RealtyUpdateView(GenericUpdateView):

    model = Realty
    form = RealtyUpdateForm
    title = title
    ref_urls = ref_urls
    readonly_fields = ['code', 'address']
    choice_fields = ['type', 'use']
    fk_fields = ['address', 'estate']
    related_data = realty_related_data
    permission_required = 'properties.change_realty'

class RealtyDeleteView(GenericDeleteView):

    title = title
    model = Realty
    form = RealtyDeleteForm
    ref_urls = ref_urls
    choice_fields = ['type', 'use']
    fk_fields = ['address', 'estate']
    related_data = realty_related_data
    permission_required = 'properties.delete_realty'
