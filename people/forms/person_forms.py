from django.forms import ModelForm, ValidationError, modelformset_factory

from adin.core.forms import GenericCreateForm, GenericUpdateForm, GenericDeleteForm
from people.models import Person, Person_Natural, Person_Legal

class PersonCreateForm(ModelForm):

    class Meta:
        model = Person
        fields = ['type']

class Person_NaturalCreateForm(GenericCreateForm):

    pk_name = 'id_number'

    class Meta:
        model = Person_Natural
        fields = ['type', 'name', 'last_name', 'id_type', 'id_number']

    def clean_type(self):
        field = self.cleaned_data.get('type')
        if field != 0:
            raise ValidationError("Debe ser persona natural.")
        return field

    def clean_id_type(self):
        field = self.cleaned_data.get('id_type')
        if field == 1:
            raise ValidationError("Tipo documento para persona natural no puede ser Nit.")
        return field

    def clean_id_number(self):
        return self.clean_pk()

class Person_LegalCreateForm(GenericCreateForm):

    pk_name = 'id_number'

    class Meta:
        model = Person_Legal
        fields = ['type', 'name', 'legal_type', 'id_type', 'id_number']

    def clean_type(self):
        field = self.cleaned_data.get('type')
        if field != 1:
            raise ValidationError("Debe ser persona jurídica.")
        return field

    def clean_id_type(self):
        field = self.cleaned_data.get('id_type')
        if field != 1:
            raise ValidationError("Tipo documento para persona jurídica debe ser Nit.")
        return field

    def clean_id_number(self):
        return self.clean_pk()

class Person_NaturalDetailForm(ModelForm):

    class Meta:
        model = Person_Natural
        fields = ['type', 'complete_name', 'id_type', 'id_number']

class Person_LegalDetailForm(ModelForm):

    class Meta:
        model = Person_Legal
        fields = ['type', 'complete_name', 'id_type', 'id_number']

class Person_NaturalUpdateForm(GenericUpdateForm):

    class Meta:
        model = Person_Natural
        fields = ['type', 'name', 'last_name', 'id_type', 'id_number']

class Person_LegalUpdateForm(GenericUpdateForm):

    class Meta:
        model = Person_Legal
        fields = ['type', 'legal_type', 'id_type', 'id_number']

class Person_NaturalDeleteForm(GenericDeleteForm):

    class Meta:
        model = Person_Natural
        fields = ['type', 'complete_name', 'id_type', 'id_number']

class Person_LegalDeleteForm(GenericDeleteForm):

    class Meta:
        model = Person_Legal
        fields = ['type', 'complete_name', 'id_type', 'id_number']

PersonListModelFormSet = modelformset_factory(Person, fields=('complete_name', 'id_type', 'id_number'), extra=0)
