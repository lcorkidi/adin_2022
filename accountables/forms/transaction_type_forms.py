from django.forms import Form, ModelChoiceField, Select, ModelForm, BaseModelFormSet, modelformset_factory, ValidationError

from adin.core.forms import GenericCreateForm, GenericActivateForm
from accountables.models import Accountable, Transaction_Type


class Transaction_TypeCreateModelForm(GenericCreateForm):

    pk_name = 'name'

    class Meta:
        model = Transaction_Type
        fields = ['name']

    def clean_name(self):
        return self.clean_pk()

class Transaction_TypeDetailModelForm(ModelForm):

    class Meta:
        model = Transaction_Type
        fields = ['state', 'name']

class Transaction_TypeDeleteModelForm(ModelForm):

    class Meta:
        model = Transaction_Type
        fields = ['name']

    exclude_fields = []

    def clean(self):
        objs = []
        for field in self.instance._meta._get_fields(forward=False, reverse=True, include_hidden=True):
            if field.related_name and field.related_query_name: 
                for obj in eval(f'self.instance.{field.related_name}.all()'):
                    objs.append(obj)
                        
        if len(objs) > 0:
            msg = f'{self.instance._meta.verbose_name} no se puede inactivar ya que tiene relación con los siguientes objetos: {objs}'
            self.add_error(None, msg)

        if self.has_changed(): 
            raise ValidationError(f'Hubo cambios en los datos inmutables del objeto.')
        return super().clean()

class Transaction_TypeActivateModelForm(GenericActivateForm):

    class Meta:
        model = Transaction_Type
        fields = ['name']

class Transaction_TypeRelatedBaseModelFormSet(BaseModelFormSet):

    def __init__(self, rel_pk, *args, **kwargs):
        super(Transaction_TypeRelatedBaseModelFormSet, self).__init__(*args, **kwargs)

Transaction_TypeListModelFormSet = modelformset_factory(Transaction_Type, fields=('state', 'name'), extra=0)

Transaction_TypeModelFormSet = modelformset_factory(Transaction_Type, formset=Transaction_TypeRelatedBaseModelFormSet, fields=('name', ), extra=0)
