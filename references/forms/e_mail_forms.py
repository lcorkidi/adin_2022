from django import forms

from references.models import E_Mail

class E_MailCreateModelForm(forms.ModelForm):

    class Meta:
        model = E_Mail
        exclude = ('e_mail',)

    def save(self, *args, **kwargs):
        base_args = {k: self.cleaned_data[k] for k in self.fields}
        base_args['state_change_user'] = self.creator
        add = E_Mail(**base_args)
        add.save()
        return add

class E_MailDetailModelForm(forms.ModelForm):

    class Meta:
        model = E_Mail
        fields = ['e_mail']

class E_MailDeleteModelForm(forms.ModelForm):

    class Meta:
        model = E_Mail
        fields = ['e_mail']

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

E_MailListModelFormSet = forms.modelformset_factory(E_Mail, fields=('e_mail',), extra=0)
