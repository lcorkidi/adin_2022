from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView
from references.models import Phone
from references.forms.phone_forms import PhoneDetailModelForm, PhoneCreateModelForm, PhoneDeleteModelForm, PhoneListModelFormSet

title = Phone._meta.verbose_name_plural
ref_urls = { 'list':'references:phone_list', 'create':'references:phone_create', 'detail':'references:phone_detail', 'delete':'references:phone_delete' }

class PhoneListView(GenericListView):

    template = 'adin/generic_list.html'
    formset = PhoneListModelFormSet
    model = Phone
    title = title
    ref_urls = ref_urls
    actions_off = ['update']
    list_order = 'code'

class PhoneCreateView(GenericCreateView):

    form = PhoneCreateModelForm
    title = title
    ref_urls = ref_urls

class PhoneDetailView(GenericDetailView):

    title = title
    model = Phone
    form = PhoneDetailModelForm
    ref_urls = ref_urls
    actions_off = ['update']

class PhoneDeleteView(GenericDeleteView):

    title = title
    model = Phone
    form = PhoneDeleteModelForm
    ref_urls = ref_urls
    actions_off = ['update']
