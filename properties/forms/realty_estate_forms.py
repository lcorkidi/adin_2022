from django.forms import modelformset_factory
from django.db.models import Sum

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm, GenericDeleteRelatedForm, GenericActivateRelatedForm
from properties.models import Realty_Estate

class Realty_EstateCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Realty_Estate
        exclude = ('state',)

    def clean(self):
        cleaned_data = super().clean()
        realty = cleaned_data.get('realty')
        percentage = cleaned_data.get('percentage')
        if self._meta.model.objects.filter(realty=realty).exclude(state=0).exists():
            total_percentage = self._meta.model.objects.filter(realty=realty).exclude(state=0).aggregate(Sum('percentage'))['percentage__sum'] + percentage
        else:
            total_percentage = percentage
        if total_percentage > 100:
            msg = f'Participación total predios ({total_percentage}) no puede sumar mas de 100.'
            self.add_error('percentage', msg)
        return cleaned_data

class Realty_EstateUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Realty_Estate
        exclude = ('state',)

    def clean(self):
        cleaned_data = super().clean()
        realty = cleaned_data.get('realty')
        percentage = cleaned_data.get('percentage')
        if self._meta.model.objects.filter(realty=realty).exclude(state=0).exists():
            total_percentage = self._meta.model.objects.filter(realty=realty).exclude(state=0).exclude(pk=self.instance.pk).aggregate(Sum('percentage'))['percentage__sum'] + percentage
        else:
            total_percentage = percentage
        if total_percentage > 100:
            msg = f'Participación total presion ({total_percentage}) no puede sumar mas de 100.'
            self.add_error('percentage', msg)
        return cleaned_data

class Realty_EstateDeleteForm(GenericDeleteRelatedForm):

    class Meta:
        model = Realty_Estate
        exclude = ('state',)

class Realty_EstateActivateForm(GenericActivateRelatedForm):

    related_fields = ['estate', 'realty']

    class Meta:
        model = Realty_Estate
        exclude = ('state',)

    def clean(self):
        cleaned_data = super().clean()
        realty = cleaned_data.get('realty')
        percentage = cleaned_data.get('percentage')
        if self._meta.model.objects.filter(realty=realty).exclude(state=0).exists():
            total_percentage = self._meta.model.objects.filter(realty=realty).exclude(state=0).aggregate(Sum('percentage'))['percentage__sum'] + percentage
        else:
            total_percentage = percentage
        if total_percentage > 100:
            msg = f'Participación total presion ({total_percentage}) no puede sumar mas de 100.'
            self.add_error('percentage', msg)
        return cleaned_data

Realty_EstateModelFormSet = modelformset_factory(Realty_Estate, fields=('state', 'estate', 'percentage'), extra=0)