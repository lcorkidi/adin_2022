from django import forms

from properties.models import Estate_Person

Estate_PersonModelFormSet = forms.modelformset_factory(Estate_Person, fields=( 'estate', 'person', 'percentage'), extra=0)