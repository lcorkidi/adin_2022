from cProfile import label
from attr import attrs
from django import forms

class LogInForm(forms.Form):

    username = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        label='Clave',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )