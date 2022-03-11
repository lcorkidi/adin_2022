from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView
from references.models import E_Mail
from references.forms.e_mail_forms import E_MailDetailModelForm, E_MailCreateModelForm, E_MailDeleteModelForm, E_MailListModelFormSet

title = E_Mail._meta.verbose_name_plural
ref_urls = { 'list':'references:e_mail_list', 'create':'references:e_mail_create', 'detail':'references:e_mail_detail', 'delete':'references:e_mail_delete' }

class E_MailListView(GenericListView):

    template = 'adin/generic_list.html'
    formset = E_MailListModelFormSet
    model = E_Mail
    title = title
    ref_urls = ref_urls
    actions_off = ['update']
    list_order = 'e_mail'

class E_MailCreateView(GenericCreateView):

    form = E_MailCreateModelForm
    title = title
    ref_urls = ref_urls

class E_MailDetailView(GenericDetailView):

    title = title
    model = E_Mail
    form = E_MailDetailModelForm
    ref_urls = ref_urls
    actions_off = ['update']

class E_MailDeleteView(GenericDeleteView):

    title = title
    model = E_Mail
    form = E_MailDeleteModelForm
    ref_urls = ref_urls
    actions_off = ['update']
