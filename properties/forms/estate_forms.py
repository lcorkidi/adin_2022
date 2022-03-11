from django import forms

from properties.models import Estate

class EstateCreateForm(forms.ModelForm):

    class Meta:
        model = Estate
        fields = [ 'national_number_1', 'national_number_2', 'national_number_2', 'address', 'total_area']

class EstateDetailForm(forms.ModelForm):

    class Meta:
        model = Estate
        fields = '__all__'

    def set_hidden_field(self, field):
        self.fields[field].widget.attrs['hidden'] = True
        self.fields[field].required = False

class EstateUpdateForm(forms.ModelForm):

    class Meta:
        model = Estate
        fields = [ 'national_number_1', 'national_number_2', 'national_number_2', 'address', 'total_area']

class EstateDeleteForm(forms.ModelForm):

    class Meta:
        model = Estate
        fields = '__all__'

EstateListModelFormSet = forms.modelformset_factory(Estate, fields=('code', 'total_area'), extra=0)