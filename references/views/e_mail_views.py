from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from adin.core.views import GenericDetailView, GenerricCreateView, GenericDeleteView
from references.models import E_Mail
from references.forms.e_mail_forms import E_MailDetailModelForm, E_MailCreateModelForm, E_MailDeleteModelForm, E_MailListModelFormSet

title = E_Mail._meta.verbose_name_plural
ref_urls = { 'list':'references:e_mail_list', 'create':'references:e_mail_create', 'detail':'references:e_mail_detail', 'delete':'references:e_mail_delete' }

class E_MailListView(LoginRequiredMixin, View):

    template = 'adin/generic_list.html'
    formset = E_MailListModelFormSet
    title = title
    ref_urls = ref_urls
    actions_off = ['update']
    list_order = 'e_mail'
    
    def get(self, request):
        formset = self.formset(queryset=E_Mail.objects.all().exclude(state=0).order_by(self.list_order))
        context = {'formset': formset, 'title': self.title, 'ref_urls': self.ref_urls, 'actions_off': self.actions_off}
        return render(request, self.template, context)

class E_MailDetailView(GenericDetailView):

    title = title
    model = E_Mail
    form = E_MailDetailModelForm
    ref_urls = ref_urls
    actions_off = ['update']

class E_MailCreateView(GenerricCreateView):

    form = E_MailCreateModelForm
    title = title
    ref_urls = ref_urls

class E_MailDeleteView(GenericDeleteView):

    title = title
    model = E_Mail
    form = E_MailDeleteModelForm
    ref_urls = ref_urls
    actions_off = ['update']
