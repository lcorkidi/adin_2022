from django.shortcuts import redirect, render

from adin.core.views import GenericListView, GenericDetailView, GenericCreateView, GenericDeleteView, GenericActivateView
from accounting.models import Ledger
from accounting.forms.ledger_forms import LedgerDetailModelForm, LedgerCreateModelForm, LedgerDeleteModelForm, LedgerActivateModelForm, LedgerListModelFormSet
from accounting.forms.charge_forms import ChargeCreateFormset
from accounting.utils import ledger_related_data, GetActionsOn, GetIncludedStates
from adin.utils.user_data import user_group_str

title = Ledger._meta.verbose_name_plural
ref_urls = { 'list':'accounting:ledger_list', 'create':'accounting:ledger_create', 'detail':'accounting:ledger_detail', 'delete':'accounting:ledger_delete', 'activate':'accounting:ledger_activate' }

class LedgerListView(GenericListView):

    formset = LedgerListModelFormSet
    model = Ledger
    title = title
    ref_urls = ref_urls
    fk_fields = ['holder', 'third_party']
    actions_on = GetActionsOn
    list_order = 'code'
    permission_required = 'accounting.view_ledger'
    include_states = GetIncludedStates

class LedgerCreateView(GenericCreateView):

    template = 'accounting/ledger_create.html'
    form = LedgerCreateModelForm
    formset = ChargeCreateFormset
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    permission_required = 'accounting.add_ledger'
    
    def get(self, request):
        form = self.form()
        formset = self.formset()
        context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'form':form, 'formset': formset, 'group': user_group_str(request.user)}
        return render(request, self.template, context)

    def post(self, request):
        form = self.form(request.POST)
        formset = self.formset(request.POST)
        if not form.is_valid() or not formset.is_valid():
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls': self.ref_urls, 'form':form, 'formset': formset, 'group': user_group_str(request.user)}
            return render(request, self.template, context)
        form.creator = request.user
        ledger = form.save()            
        formset.creator = request.user
        formset.save(ledger)
        return redirect(self.ref_urls['list'])

class LedgerDetailView(GenericDetailView):

    title = title
    model = Ledger
    form = LedgerDetailModelForm
    ref_urls = ref_urls
    fk_fields = ['holder', 'third_party']
    actions_on = GetActionsOn
    related_data = ledger_related_data
    permission_required = 'accounting.view_ledger'

class LedgerDeleteView(GenericDeleteView):

    title = title
    model = Ledger
    form = LedgerDeleteModelForm
    ref_urls = ref_urls
    fk_fields = ['holder', 'third_party']
    actions_on = GetActionsOn
    related_data = ledger_related_data
    permission_required = 'accounting.delete_ledger'

class LedgerActivateView(GenericActivateView):

    title = title
    model = Ledger
    form = LedgerActivateModelForm
    ref_urls = ref_urls
    fk_fields = ['holder', 'third_party']
    actions_on = GetActionsOn
    related_data = ledger_related_data
    permission_required = 'accounting.activate_ledger'

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        if self.related_data:
            related_data = self.related_data()
            for attr, data in related_data.items():
                filter_expresion = {}
                filter_expresion[data['filter_expresion']] = pk
                formset = data['formset'](queryset=data['class'].objects.filter(**filter_expresion), rel_pk=pk)
                related_data[attr]['formset'] = formset
        else:
            related_data = None
        if not form.is_valid():
            actions_on = self.actions_on(request.user, self.model.__name__)
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'form':form, 'related_data':related_data, 'choice_fields':self.choice_fields, 'fk_fields': self.fk_fields, 'actions_on': actions_on}
            return render(request, self.template, context)
        if related_data:    
            for key, data in related_data.items():
                for form in data['formset']:
                    ins = form.instance
                    ins.state = 2
                    ins.save()
        obj.state = 2
        obj.save()
        return redirect(self.ref_urls['detail'], obj.pk)
