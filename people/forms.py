from django import forms
from .models import Person

PersonListModelFormSet = forms.modelformset_factory(Person, fields=('complete_name', 'id_type', 'id_number'), extra=0)