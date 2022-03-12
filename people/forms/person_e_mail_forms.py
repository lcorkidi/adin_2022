from django.forms import modelformset_factory

from adin.core.forms import GeneriCreateRelatedForm, GenericUpdateRelatedForm
from people.models import Person_E_Mail

class Person_EmailCreateForm(GeneriCreateRelatedForm):

    class Meta:
        model = Person_E_Mail
        fields = '__all__'

class Person_EmailUpdateForm(GenericUpdateRelatedForm):

    class Meta:
        model = Person_E_Mail
        fields = '__all__'

Person_EmailModelFormSet = modelformset_factory(Person_E_Mail, fields=('e_mail', 'use'), extra=0)
