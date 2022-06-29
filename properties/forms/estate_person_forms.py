from django.forms import modelformset_factory
from django.db.models import Sum

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm, GenericDeleteRelatedForm, GenericActivateRelatedForm
from properties.models import Estate_Person

class Estate_PersonCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Estate_Person
        exclude = ('state',)

    def clean_person(self):
        person = self.cleaned_data['person']
        if person.state == 0:
            self.add_error('person', f'Persona seleccionada inactiva.')
        return person

    def clean(self):
        cleaned_data = super().clean()
        estate = cleaned_data.get('estate')
        percentage = cleaned_data.get('percentage')
        if self._meta.model.objects.filter(estate=estate).exclude(state=0).exists():
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
        exclude = ('state',)

    def clean(self):
        cleaned_data = super().clean()
        estate = cleaned_data.get('estate')
        percentage = cleaned_data.get('percentage')
        if self._meta.model.objects.filter(estate=estate).exclude(state=0).exclude(pk=self.instance.pk).exists():
            print(percentage)
            total_percentage = self._meta.model.objects.filter(estate=estate).exclude(state=0).exclude(pk=self.instance.pk).aggregate(Sum('percentage'))['percentage__sum'] + percentage
        else:
            total_percentage = percentage
        if total_percentage > 100:
            msg = f'Participación total propietarios ({total_percentage}) no puede sumar mas de 100.'
            self.add_error('percentage', msg)
        return cleaned_data

class Estate_PersonDeleteForm(GenericDeleteRelatedForm):

    class Meta:
        model = Estate_Person
        exclude = ('state',)

class Estate_PersonActivateForm(GenericActivateRelatedForm):

    related_fields = ['estate', 'person']

    class Meta:
        model = Estate_Person
        exclude = ('state',)

    def clean(self):
        cleaned_data = super().clean()
        estate = cleaned_data.get('estate')
        percentage = cleaned_data.get('percentage')
        if self._meta.model.objects.filter(estate=estate).exclude(state=0).exists():
            total_percentage = self._meta.model.objects.filter(estate=estate).exclude(state=0).aggregate(Sum('percentage'))['percentage__sum'] + percentage
        else:
            total_percentage = percentage
        if total_percentage > 100:
            msg = f'Participación total propietarios ({total_percentage}) no puede sumar mas de 100.'
            self.add_error('percentage', msg)
        return cleaned_data

Estate_PersonModelFormSet = modelformset_factory(Estate_Person, fields=('state', 'person', 'percentage'), extra=0)