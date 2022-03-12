from django import forms

from properties.models.estate import Estate_Appraisal

class Estate_AppraisalCreateForm(forms.ModelForm):

    class Meta:
        model = Estate_Appraisal
        fields = '__all__'

    def save(self, *args, **kwargs):
        base_args = {k: self.cleaned_data[k] for k in self.fields}
        base_args['state_change_user'] = self.creator
        per_pho = Estate_Appraisal(**base_args)
        per_pho.save()

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

class Estate_AppraisalUpdateForm(forms.ModelForm):

    class Meta:
        model = Estate_Appraisal
        fields = '__all__'

    def save(self, *args, **kwargs):
        for delta in self.changed_data:
            if delta in args[0]:
                raise forms.ValidationError('No se puede actualizar con esos cambios.')
        get_args = {}
        update_args = {}
        for k in self.fields:
            if k in args[0]:
                get_args[k] = self.cleaned_data[k]
            elif k in self.changed_data:
                update_args[k] = self.cleaned_data[k]
        per_pho = Estate_Appraisal.objects.get(**get_args)
        for k, v in update_args.items():
            setattr(per_pho, k, v)
        per_pho.state_change_date = self.creator
        per_pho.save()

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

    def set_readonly_fields(self, fields=[]):
        for field in self.fields:
            if field in fields:
                self.fields[field].widget.attrs['readonly'] = True
            else: 
                self.fields[field].widget.attrs['readonly'] = False

Estate_AppraisalModelFormSet = forms.modelformset_factory(Estate_Appraisal, fields=('type', 'date', 'value'), extra=0)