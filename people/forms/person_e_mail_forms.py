from django.forms import BaseModelFormSet, modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm, GenericDeleteRelatedForm, GenericActivateRelatedForm
from people.models import Person_E_Mail

class Person_E_MailCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Person_E_Mail
        exclude = ('state',)

    def clean_e_mail(self):
        e_mail = self.cleaned_data['e_mail']
        if e_mail.state == 0:
            self.add_error('e_mail', f'Correo seleccionado inactivo.')
        return e_mail

class Person_E_MailUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Person_E_Mail
        exclude = ('state',)

class Person_E_MailDeleteForm(GenericDeleteRelatedForm):

    class Meta:
        model = Person_E_Mail
        exclude = ('state',)

class Person_E_MailActivateForm(GenericActivateRelatedForm):

    related_fields = ['person', 'e_mail']

    class Meta:
        model = Person_E_Mail
        exclude = ('state',)

class Person_E_MailRelatedBaseModelFormSet(BaseModelFormSet):

    def __init__(self, rel_pk, *args, **kwargs):
        super(Person_E_MailRelatedBaseModelFormSet, self).__init__(*args, **kwargs)

Person_E_MailModelFormSet = modelformset_factory(Person_E_Mail, formset=Person_E_MailRelatedBaseModelFormSet, fields=('state', 'e_mail', 'use'), extra=0)
