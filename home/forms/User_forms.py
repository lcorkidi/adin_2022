from django.forms import Form, CharField, TextInput, PasswordInput

class UserLogInForm(Form):

    username = CharField(
        label='Nombre',
        widget=TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = CharField(
        label='Clave',
        widget=PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class UserRegisterForm(Form):

    username = CharField(
        label='Nombre',
        widget=TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = CharField(
        label='Clave',
        widget=PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = CharField(
        label='Repetir Clave',
        widget=PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

