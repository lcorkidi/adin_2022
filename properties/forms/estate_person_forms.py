from django.forms import modelformset_factory
from django.db.models import Sum

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm
from properties.models import Estate_Person

class Estate_PersonCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Estate_Person
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        estate = cleaned_data.get('estate')
        percentage = cleaned_data.get('percentage')
        if self._meta.model.objects.filter(estate=estate).exists():
            total_percentage = self._meta.model.objects.filter(estate=estate).exclude(state=0).aggregate(Sum('percentage'))['percentage__sum'] + percentage
        else:
            total_percentage = percentage
        if total_percentage > 100:
            msg = f'Participación total propietarios ({total_percentage}) no puede sumar mas de 100.'
            self.add_error('percentage', msg)
        return cleaned_data

class Estate_PersonUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Estate_Person
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        estate = cleaned_data.get('estate')
        percentage = cleaned_data.get('percentage')
        total_percentage = self._meta.model.objects.filter(estate=estate).exclude(state=0).aggregate(Sum('percentage'))['percentage__sum'] + percentage
        if total_percentage > 100:
            msg = f'Participación total propietarios ({total_percentage}) no puede sumar mas de 100.'
            self.add_error('percentage', msg)
        return cleaned_data

Estate_PersonModelFormSet = modelformset_factory(Estate_Person, fields=( 'person', 'percentage'), extra=0)