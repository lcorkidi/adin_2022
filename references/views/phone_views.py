from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView, GenericActivateView
from references.models import Phone
from references.forms.phone_forms import PhoneDetailModelForm, PhoneCreateModelForm, PhoneDeleteModelForm, PhoneActivateModelForm, PhoneListModelFormSet
from references.utils import GetActionsOn, GetIncludedStates

title = Phone._meta.verbose_name_plural
ref_urls = { 'list':'references:phone_list', 'create':'references:phone_create', 'detail':'references:phone_detail', 'delete':'references:phone_delete', 'activate':'references:phone_activate' }

class PhoneListView(GenericListView):

    formset = PhoneListModelFormSet
    model = Phone
    title = title
    ref_urls = ref_urls
    actions_on = GetActionsOn
    list_order = 'code'
    permission_required = 'references.view_phone'
    include_states = GetIncludedStates

class PhoneCreateView(GenericCreateView):

    form = PhoneCreateModelForm
    title = title
    ref_urls = ref_urls
    permission_required = 'references.add_phone'

class PhoneDetailView(GenericDetailView):

    title = title
    model = Phone
    form = PhoneDetailModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'references.view_phone'

class PhoneDeleteView(GenericDeleteView):

    title = title
    model = Phone
    form = PhoneDeleteModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'references.delete_phone'

class PhoneActivateView(GenericActivateView):

    title = title
    model = Phone
    form = PhoneActivateModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'references.activate_phone'
    success_url = 'list'