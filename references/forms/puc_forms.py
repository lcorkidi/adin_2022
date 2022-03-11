from django import forms

from references.models import PUC

PUCListModelFormSet = forms.modelformset_factory(PUC, fields=('code', 'name'), extra=0)
