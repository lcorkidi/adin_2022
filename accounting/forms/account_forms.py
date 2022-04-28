from django.forms import ModelForm, ValidationError, modelformset_factory

from adin.core.forms import GenericCreateForm, GenericUpdateForm, GenericDeleteForm, GenericActivateForm
from accounting.models import Account

class AccountCreateForm(GenericCreateForm):

    pk_name = 'code'

    class Meta:
        model = Account
        fields = [ 'code', 'name' ]

    def clean_code(self):
        code = self.clean_pk()
        code_str = str(code)
        code_len = len(str(code))
        if code_len in [3, 5, 7, 9] or code_len > 10:
            raise ValidationError('Numero de digitos del código no puede ser igual a 3, 5, 7, 9 o mayor que 10.')
        if code_len in [1, 2]:
            parent_code = int(code_str[:1])
        else:
            parent_code = int(code_str[:code_len - 2])
        if not Account.objects.filter(code=parent_code).exists():
            raise ValidationError(f'Cuenta padre {parent_code} no existe.')
        if len(Account.objects.get(pk=parent_code).charges.all()) > 0:
            msg = f'Cuenta no se puede inactivar ya que cuenta padre tiene movimientos.'
            self.add_error(None, msg)
        return code

class AccountDetailForm(ModelForm):

    class Meta:
        model = Account
        fields = [ 'code', 'name' ]

class AccountUpdateForm(GenericUpdateForm):

    class Meta:
        model = Account
        fields = [ 'code', 'name' ]

class AccountDeleteForm(GenericDeleteForm):

    class Meta:
        model = Account
        fields = [ 'code', 'name' ]

    def clean(self):
        cleaned_data = super().clean()
        code = cleaned_data.get('code')
        if Account.objects.filter(code__startswith=code).exclude(code=code).exclude(state=0).exists():
            msg = f'Cuenta no se puede inactivar ya que tiene las siguientes cuentas hijo: {list(Account.objects.filter(code__startswith=code).exclude(code=code).exclude(state=0))}'
            self.add_error(None, msg)
        if len(self.instance.charges.all()) > 0:
            msg = f'Cuenta no se puede inactivar ya que tiene movimientos.'
            self.add_error(None, msg)
        return cleaned_data

class AccountActivateForm(GenericActivateForm):

    class Meta:
        model = Account
        fields = [ 'code', 'name' ]

AccountListModelFormSet = modelformset_factory(Account, fields=('state', 'code', 'name'), extra=0)