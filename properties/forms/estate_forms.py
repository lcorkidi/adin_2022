from django import forms

from properties.models import Estate

EstateListModelFormSet = forms.modelformset_factory(Estate, fields=('code', 'total_area'), extra=0)