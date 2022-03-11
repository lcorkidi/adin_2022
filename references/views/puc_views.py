from django.shortcuts import render
from django.db.models.functions import Cast
from django.db.models.fields import CharField

from adin.core.views import GenericListView, GenericCreateBulkView, GenericDeleteBulkView
from references.models import PUC
from references.forms.puc_forms import PUCListModelFormSet

title = PUC._meta.verbose_name_plural
ref_urls = { 'list':'references:puc_list', 'create':'references:puc_create', 'detail':'references:puc_detail', 'delete':'references:puc_delete' }

class PUCListView(GenericListView):

    template = 'adin/generic_list_bulk.html'
    formset = PUCListModelFormSet
    title = title
    ref_urls = ref_urls
    list_order = 'code'
    
    def get(self, request):
        if PUC.objects.all().exists():
            actions_off = ['detail', 'create']
        else:
            actions_off = ['detail', 'delete']
        formset = self.formset(queryset=PUC.objects.annotate(char_code=Cast('code', CharField())).order_by('char_code')[:50])
        context = {'formset': formset, 'title': self.title, 'ref_urls': self.ref_urls, 'actions_off': actions_off}
        return render(request, self.template, context)
    permission_required = 'people.view_puc'

class PUCCreateView(GenericCreateBulkView):

    title = title
    ref_urls = ref_urls
    permission_required = 'people.add_puc'

class PUCDeleteView(GenericDeleteBulkView):

    title = title
    model = PUC
    ref_urls = ref_urls
    permission_required = 'people.delete_puc'
    
