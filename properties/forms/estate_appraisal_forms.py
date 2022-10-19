from django.forms import BaseModelFormSet, modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm, GenericDeleteRelatedForm, GenericActivateRelatedForm
from adin.core.widgets import SelectDateSpanishWidget
from properties.models.estate import Estate_Appraisal

class Estate_AppraisalCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Estate_Appraisal
        exclude = ('state',)
        widgets = {
            'date': SelectDateSpanishWidget()
        }

class Estate_AppraisalUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Estate_Appraisal
        exclude = ('state',)
        widgets = {
            'date': SelectDateSpanishWidget()
        }

class Estate_AppraisalDeleteForm(GenericDeleteRelatedForm):

    class Meta:
        model = Estate_Appraisal
        exclude = ('state',)
        widgets = {
            'date': SelectDateSpanishWidget()
        }

class Estate_AppraisalActivateForm(GenericActivateRelatedForm):

    class Meta:
        model = Estate_Appraisal
        exclude = ('state',)
        widgets = {
            'date': SelectDateSpanishWidget()
        }

class Estate_AppraisalRelatedBaseModelFormSet(BaseModelFormSet):

    def __init__(self, rel_pk, *args, **kwargs):
        super(Estate_AppraisalRelatedBaseModelFormSet, self).__init__(*args, **kwargs)

Estate_AppraisalModelFormSet = modelformset_factory(Estate_Appraisal, formset=Estate_AppraisalRelatedBaseModelFormSet, fields=('state', 'type', 'date', 'value'), extra=0)