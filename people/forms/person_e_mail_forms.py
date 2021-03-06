from django.forms import modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm, GenericDeleteRelatedForm, GenericActivateRelatedForm
from people.models import Person_E_Mail

class Person_E_MailCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Person_E_Mail
        exclude = ('state',)

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

Person_E_MailModelFormSet = modelformset_factory(Person_E_Mail, fields=('state', 'e_mail', 'use'), extra=0)
