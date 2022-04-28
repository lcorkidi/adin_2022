import datetime
from django.forms import Form, CharField, ModelChoiceField, ModelForm, SelectDateWidget, modelformset_factory, ValidationError

from adin.core.forms import GenericCreateForm, GenericActivateForm
from references.models import Charge_Factor, Factor_Data
from accounting.models import Charge

class Charge_FactorCreateForm(Form):

    name = CharField(
        required=False,
        label='Nombre Tasa Nueva'
    )
    factor = ModelChoiceField(
        queryset=Charge_Factor.objects.all(),
        required=False,
        label='Tasa existente'
    )

    def clean(self):
        data = super().clean()
        name = data.get('name')
        factor = data.get('factor')
        if not name and not factor:
            msg = 'Se debe llenar campo para nombre o seleccionar tasa.'
            self.add_error(None, msg)
        if name and factor:
            msg = 'Solo se debe llenar el campo para nombre o seleccionar tasa.'
            self.add_error(None, msg)
        return data

    def save(self):
        data = self.cleaned_data
        name = data.get('name')
        factor = data.get('factor')
        if name:
            if Charge_Factor.objects.filter(name=name).exists():
                return Charge_Factor.objects.get(name=name)
            else:
                base_args = {}
                base_args['name'] = name
                base_args['state_change_user'] = self.creator
                obj = Charge_Factor(**base_args)
                obj.save()
                return obj
        else:
            return factor

class Factor_DataCreateForm(GenericCreateForm):

    class Meta:
        model = Factor_Data
        fields = ['factor', 'validity_date', 'amount', 'percentage', 'in_instance_attribute']
        widgets = {
            'validity_date': SelectDateWidget(
                years=range(1970, datetime.date.today().year + 1),
                months= {
                    1: 'Enero',
                    2: 'Febrero',
                    3: 'Marzo',
                    4: 'Abril',
                    5: 'Mayo',
                    6: 'Junio',
                    7: 'Julio',
                    8: 'Agosto',
                    9: 'Septiembre',
                    10: 'Octubre',
                    11: 'Noviembre',
                    12: 'Diciembre'
                }
            )
        }

class Factor_DataDetailForm(ModelForm):

    class Meta:
        model = Factor_Data
        fields = ['factor', 'validity_date', 'amount', 'percentage', 'in_instance_attribute']

class Factor_DataDeleteForm(ModelForm):

    class Meta:
        model = Factor_Data
        fields = ['factor', 'validity_date', 'amount', 'percentage', 'in_instance_attribute']

    def clean(self):
        tra_typs = []
        accs = []
        for cha_tem in self.instance.factor.charges_templates.all():
            tra_typs.append(cha_tem.ledger_template.transaction_type)
            accs.append(cha_tem.account)
            objs = []
        for obj in Charge.active.filter(ledger__date__gte=self.instance.validity_date, ledger__date__lt=self.instance.validity_end_date(), concept__transaction_type__in=tra_typs, account__in=accs):
            objs.append(obj)
        if len(objs) > 0:
            msg = f'La tasa no se puede inactivar ya que tiene relación con los siguientes objetos: {objs}'
            self.add_error(None, msg)
        if self.has_changed(): 
            raise ValidationError(f'Hubo cambios en los datos inmutables del objeto.')
        return super().clean()

class Factor_DataActivateModelForm(GenericActivateForm):

    class Meta:
        model = Factor_Data
        fields = ['factor', 'validity_date', 'amount', 'percentage', 'in_instance_attribute']

Factor_DataListModelFormSet = modelformset_factory(Factor_Data, fields=('state', 'factor', 'validity_date', 'amount', 'percentage', 'in_instance_attribute'), extra=0)