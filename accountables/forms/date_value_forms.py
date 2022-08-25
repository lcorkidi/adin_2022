from django.forms import modelformset_factory, formset_factory, Form, DateField

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm, GenericDeleteRelatedForm, GenericActivateRelatedForm
from accountables.models import Date_Value
from adin.core.widgets import SelectDateSpanishWidget

class Date_ValueCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Date_Value
        exclude = ('state',)
        widgets = {
            'date': SelectDateSpanishWidget()
        }

class DateValuePendingDateForm(Form):

    date = DateField(
        label='Fecha'
    )

class Date_ValueUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Date_Value
        exclude = ('state',)
        widgets = {
            'date': SelectDateSpanishWidget()
        }

class Date_ValueDeleteForm(GenericDeleteRelatedForm):

    class Meta:
        model = Date_Value
        exclude = ('state',)
        widgets = {
            'date': SelectDateSpanishWidget()
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        if date == self.instance.date:
            self.add_error(None, 'Canon para la fecha del contrato no se puede deactivar.')
        return date

class Date_ValueActivateForm(GenericActivateRelatedForm):

    class Meta:
        model = Date_Value
        exclude = ('state',)
        widgets = {
            'date': SelectDateSpanishWidget()
        }

Date_ValueModelFormSet = modelformset_factory(Date_Value, fields=('state', 'date', 'value'), extra=0)

Date_ValuePendingDateFormset = formset_factory(DateValuePendingDateForm, extra=0)