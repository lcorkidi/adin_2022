from django.forms import modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm
from properties.models import Estate_Person

class Estate_PersonCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Estate_Person
        fields = '__all__'

class Estate_PersonUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Estate_Person
        fields = '__all__'

Estate_PersonModelFormSet = modelformset_factory(Estate_Person, fields=( 'person', 'percentage'), extra=0)