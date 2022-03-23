from django.forms import modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm
from accountables.models import Date_Value

class Date_ValueCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Date_Value
        fields = '__all__'

class Date_ValueUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Date_Value
        fields = '__all__'

Date_ValueModelFormSet = modelformset_factory(Date_Value, fields=( 'date', 'value'), extra=0)