from django.forms import ModelForm, modelformset_factory

from adin.core.forms import GenericCreateForm, GenericDeleteForm
from references.models import E_Mail

class E_MailCreateModelForm(GenericCreateForm):

    pk_name = 'e_mail'

    class Meta:
        model = E_Mail
        fields = ['e_mail']

    def clean_e_mail(self):
        return self.clean_pk()

class E_MailDetailModelForm(ModelForm):

    class Meta:
        model = E_Mail
        fields = ['e_mail']

class E_MailDeleteModelForm(GenericDeleteForm):

    class Meta:
        model = E_Mail
        fields = ['e_mail']

E_MailListModelFormSet = modelformset_factory(E_Mail, fields=('state', 'e_mail',), extra=0)
