from django.shortcuts import redirect, render

from adin.core.views import GenericCreateRelatedView, GenericUpdateRelatedView, GenericDeleteRelatedView, GenericActivateRelatedView
from properties.models import Realty_Estate
from properties.forms.realty_estate_forms import Realty_EstateCreateForm, Realty_EstateUpdateForm, Realty_EstateDeleteForm, Realty_EstateActivateForm
from adin.utils.user_data import user_group_str

title = Realty_Estate._meta.verbose_name_plural
ref_urls = { 'list':'properties:realty_list', 'create':'properties:realty_create', 'detail':'properties:realty_detail', 'update':'properties:realty_update', 'delete':'properties:realty_delete' }
rel_urls = { 'create': 'properties:realty_estate_create', 'delete': 'properties:realty_estate_delete', 'update': 'properties:realty_estate_update' }

class Realty_EstateCreateView(GenericCreateRelatedView):

    form = Realty_EstateCreateForm
    title = title
    subtitle = 'Crear'
    ref_urls = ref_urls
    readonly_fields = ['realty']
    fk_fields = ['realty']
    permission_required = 'properties.add_realty_estate'
    related_fields = ['realty', 'estate']

class Realty_EstateUpdateView(GenericUpdateRelatedView):

    model = Realty_Estate
    form = Realty_EstateUpdateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    readonly_fields = ['realty', 'estate']
    fk_fields = ['realty', 'estate']
    permission_required = 'properties.change_realty_estate'

class Realty_EstateDeleteView(GenericDeleteRelatedView):

    model = Realty_Estate
    form = Realty_EstateDeleteForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    fk_fields = ['realty', 'estate']
    permission_required = 'properties.delete_realty_estate'

class Realty_EstateActivateView(GenericActivateRelatedView):

    model = Realty_Estate
    form = Realty_EstateActivateForm
    title = title
    ref_urls = ref_urls
    rel_urls = rel_urls
    fk_fields = ['realty', 'estate']
    permission_required = 'properties.activate_realty'

    def post(self, request, ret_pk, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        if not form.is_valid():
            context = {'title':self.title, 'subtitle':self.subtitle, 'ref_urls':self.ref_urls, 'rel_urls':self.rel_urls, 'fk_fields': self.fk_fields, 'form':form, 'ref_pk': ret_pk, 'choice_fields':self.choice_fields, 'group': user_group_str(request.user)}
            return render(request, self.template, context)
        obj.state = 2
        obj.save()
        return redirect(self.ref_urls['update'], ret_pk)
