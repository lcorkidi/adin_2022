from django.forms import modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm
from properties.models.estate import Estate_Appraisal

class Estate_AppraisalCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Estate_Appraisal
        fields = '__all__'

class Estate_AppraisalUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Estate_Appraisal
        fields = '__all__'

Estate_AppraisalModelFormSet = modelformset_factory(Estate_Appraisal, fields=('type', 'date', 'value'), extra=0)