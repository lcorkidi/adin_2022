from django.forms import modelformset_factory, formset_factory, Form, DateField, ModelForm, BaseModelFormSet
from accountables.models.accountable import Accountable

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

    def clean(self):
        if self.instance.date:
            self.add_error(None, 'Canon para la fecha del contrato no se puede deactivar.')
        return super().clean()

class Date_ValueActivateForm(GenericActivateRelatedForm):

    class Meta:
        model = Date_Value
        exclude = ('state',)
        widgets = {
            'date': SelectDateSpanishWidget()
        }

Date_ValueModelFormSet = modelformset_factory(Date_Value, fields=('state', 'date', 'value'), extra=0)

Date_ValuePendingDateFormset = formset_factory(DateValuePendingDateForm, extra=0)

class Date_ValueRelatedUpdateModelForm(ModelForm):

    def add_errors(self):
        print(self.instance)

class Date_ValueRelatedUpdateBaseModelFormSet(BaseModelFormSet):

    def __init__(self, rel_pk, *args, **kwargs):
        super(Date_ValueRelatedUpdateBaseModelFormSet, self).__init__(*args, **kwargs)
        self.add_errors(rel_pk)

    def add_errors(self, rel_pk):
        formset_errors = []
        acc = Accountable.objects.get(pk=rel_pk)
        print(acc.get_date_value_errors())
        if acc.get_date_value_errors():
            for error in acc.get_date_value_errors():
                formset_errors.append(error)
        if formset_errors:
            self.formset_errors = formset_errors
        for form in self.forms:
            form.add_errors()

Date_ValueRelatedUpdateModelFormSet = modelformset_factory(Date_Value, form=Date_ValueRelatedUpdateModelForm, formset=Date_ValueRelatedUpdateBaseModelFormSet, fields=('state', 'date', 'value'), extra=0)