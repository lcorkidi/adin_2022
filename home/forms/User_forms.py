from django import forms

class UserLogInForm(forms.Form):

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