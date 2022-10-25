from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView, GenericActivateView
from references.models import E_Mail
from references.forms.e_mail_forms import E_MailDetailModelForm, E_MailCreateModelForm, E_MailDeleteModelForm, E_MailActivateModelForm, E_MailListModelFormSet
from references.utils import GetActionsOn, GetIncludedStates

title = E_Mail._meta.verbose_name_plural
ref_urls = { 'list':'references:e_mail_list', 'create':'references:e_mail_create', 'detail':'references:e_mail_detail', 'delete':'references:e_mail_delete', 'activate':'references:e_mail_activate' }

class E_MailListView(GenericListView):

    formset = E_MailListModelFormSet
    model = E_Mail
    title = title
    ref_urls = ref_urls
    actions_on = GetActionsOn
    list_order = 'e_mail'
    permission_required = 'references.view_e_mail'
    include_states = GetIncludedStates

class E_MailCreateView(GenericCreateView):

    form = E_MailCreateModelForm
    title = title
    ref_urls = ref_urls
    permission_required = 'references.add_e_mail'

class E_MailDetailView(GenericDetailView):

    title = title
    model = E_Mail
    form = E_MailDetailModelForm
    ref_urls = ref_urls
    actions_on = GetActionsOn
    permission_required = 'references.view_e_mail'

class E_MailDeleteView(GenericDeleteView):

    title = title
    model = E_Mail
    form = E_MailDeleteModelForm
    ref_urls = ref_urls
    actions_on = GetActionsOn
    permission_required = 'references.delete_e_mail'

class E_MailActivateView(GenericActivateView):

    title = title
    model = E_Mail
    form = E_MailActivateModelForm
    ref_urls = ref_urls
    actions_on = GetActionsOn
    permission_required = 'references.activate_e_mail'
    success_url = 'list'