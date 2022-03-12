from django import forms

from properties.models import Estate
from properties.utils impo

class EstateCreateForm(forms.ModelForm):

    class Meta:
        model = Estate
        fields = [ 'national_number_1', 'national_number_2', 'national_number_3', 'address', 'total_area']

    def clean_id_number(self):
        field = self.cleaned_data.get('address')

        if Estate.objects.filter(pk=field).exists():
            obj = Estate.objects.get(pk=field)
            if obj.state == 0:
                raise forms.ValidationError("Persona con número de documento ya existe y está inactiva.")
            else:
                raise forms.ValidationError("Persona con número de documento ya existe.")
        return field

    def save(self, *args, **kwargs):
        base_args = {k: self.cleaned_data[k] for k in self.fields}
        base_args['state_change_user'] = self.creator
        per_nat = Estate(**base_args)
        per_nat.save()
        return per_nat

class EstateDetailForm(forms.ModelForm):

    class Meta:
        model = Estate
        fields = [ 'national_number_1', 'national_number_2', 'national_number_3', 'code', 'address', 'total_area']

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

class EstateDeleteForm(forms.ModelForm):

    class Meta:
        model = Estate
        fields = [ 'national_number_1', 'national_number_2', 'national_number_3', 'code', 'address', 'total_area']

    def clean(self):
        objs = []
        for obj in self.instance._meta._get_fields(forward=False, reverse=True, include_hidden=True):
            if (not obj.hidden or obj.field.many_to_many) and obj.related_name: 
                for obj in eval(f'self.instance.{obj.related_name}.all()'):
                    objs.append(obj)
        if len(objs) > 0:
            msg = f'Direccion no se puede inactivar ya que tiene relación con los siguientes objetos: {objs}'
            self.add_error(None, msg)

        if self.has_changed(): 
            self.add_error(None, f'Hubo cambios en los datos del objeto.')

EstateListModelFormSet = forms.modelformset_factory(Estate, fields=('code', 'total_area'), extra=0)