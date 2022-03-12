from django import forms

from properties.models import Estate

class EstateCreateForm(forms.ModelForm):

    class Meta:
        model = Estate
        fields = [ 'national_number_1', 'national_number_2', 'national_number_3', 'address', 'total_area']

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

    def set_hidden_field(self, field):
        self.fields[field].widget.attrs['hidden'] = True
        self.fields[field].required = False

class EstateUpdateForm(forms.ModelForm):

    class Meta:
        model = Estate
        fields = [ 'national_number_1', 'national_number_2', 'national_number_3', 'code', 'address', 'total_area']

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

    def set_hidden_field(self, field):
        self.fields[field].widget.attrs['hidden'] = True
        self.fields[field].required = False

class EstateDeleteForm(forms.ModelForm):

    class Meta:
        model = Estate
        fields = [ 'national_number_1', 'national_number_2', 'national_number_3', 'code', 'address', 'total_area']

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

    def set_hidden_field(self, field):
        self.fields[field].widget.attrs['hidden'] = True
        self.fields[field].required = False

EstateListModelFormSet = forms.modelformset_factory(Estate, fields=('code', 'total_area'), extra=0)