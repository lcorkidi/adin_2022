
from django.forms import BaseModelFormSet, modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericDetailRelatedForm, GenericUpdateRelatedForm, GenericDeleteRelatedForm, GenericActivateRelatedForm
from accountables.models import Accountable_Transaction_Type

class Accountable_Transaction_TypeCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Accountable_Transaction_Type
        exclude = ('state',)

class Accountable_Transaction_TypeDetailForm(GenericDetailRelatedForm):

    class Meta:
        model = Accountable_Transaction_Type
        exclude = ('state',)

class Accountable_Transaction_TypeUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Accountable_Transaction_Type
        exclude = ('state',)

class Accountable_Transaction_TypeDeleteForm(GenericDeleteRelatedForm):

    class Meta:
        model = Accountable_Transaction_Type
        exclude = ('state',)

class Accountable_Transaction_TypeActivateForm(GenericActivateRelatedForm):

    class Meta:
        model = Accountable_Transaction_Type
        exclude = ('state',)


class Accountable_Transaction_TypeRelatedBaseModelFormSet(BaseModelFormSet):

    def __init__(self, rel_pk, *args, **kwargs):
        super(Accountable_Transaction_TypeRelatedBaseModelFormSet, self).__init__(*args, **kwargs)
                
Accountable_Transaction_TypeModelFormSet = modelformset_factory(Accountable_Transaction_Type, formset=Accountable_Transaction_TypeRelatedBaseModelFormSet, fields=('state', 'transaction_type', 'ledger_template', 'date_applicable'), extra=0)
