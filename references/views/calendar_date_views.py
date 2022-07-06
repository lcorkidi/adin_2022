from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView, GenericActivateView
from references.models import Calendar_Date
from references.forms.calendar_date_forms import Calendar_DateCreateForm, Calendar_DateDetailModelForm, Calendar_DateDeleteModelForm, Calendar_DateActivateModelForm, Calendar_DateListModelFormSet

title = Calendar_Date._meta.verbose_name_plural
ref_urls = { 'list':'references:calendar_date_list', 'create':'references:calendar_date_create', 'detail':'references:calendar_date_detail', 'delete':'references:calendar_date_delete', 'activate':'references:calendar_date_activate' }

class Calendar_DateListView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'references.view_calendar_date'

    def get(self, request):
        if request.user.has_perm('references.activate_calendar_date'):
            return redirect('references:calendar_date_list_all')
        else: 
            return redirect('references:calendar_date_list_some')

class Calendar_DateListSomeView(GenericListView):

    template = 'adin/generic_list.html'
    formset = Calendar_DateListModelFormSet
    model = Calendar_Date
    title = title
    ref_urls = ref_urls
    actions_off = ['update']
    list_order = 'name'
    permission_required = 'references.view_calendar_date'

class Calendar_DateListAllView(GenericListView):

    template = 'adin/generic_list.html'
    formset = Calendar_DateListModelFormSet
    model = Calendar_Date
    title = title
    ref_urls = ref_urls
    actions_off = ['update']
    list_order = 'name'
    permission_required = 'references.activate_calendar_date'
    include_states = [ 0, 1, 2, 3 ]

class Calendar_DateCreateView(GenericCreateView):

    form = Calendar_DateCreateForm
    title = title
    ref_urls = ref_urls
    permission_required = 'references.add_calendar_date'

class Calendar_DateDetailView(GenericDetailView):

    title = title
    model = Calendar_Date
    form = Calendar_DateDetailModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'references.view_calendar_date'

class Calendar_DateDeleteView(GenericDeleteView):

    title = title
    model = Calendar_Date
    form = Calendar_DateDeleteModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'references.delete_calendar_date'

class Calendar_DateActivateView(GenericActivateView):

    title = title
    model = Calendar_Date
    form = Calendar_DateActivateModelForm
    ref_urls = ref_urls
    actions_off = ['update']
    permission_required = 'references.activate_calendar_date'
    success_url = 'list'