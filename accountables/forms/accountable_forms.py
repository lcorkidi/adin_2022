from django.forms import ModelForm

from accountables.models import Accountable

class AccountableAccoutingForm(ModelForm):

    class Meta:
        model = Accountable
        fields = ['state',  'code']
