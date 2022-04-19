from django.db import models
from django.db.models import F
from django.db.models.functions import Cast
from django.db.models.fields import CharField

from accounting.core import Account_Structure
from adin.core.models import BaseModel

class Chargeables(models.Manager):
    def code_list(self):
        return self.get_queryset().values_list('code', flat=True)

    def get_queryset(self):
        try:
            chargeables = []
            level1_list = super().get_queryset().filter(code__regex=r'^[0-9]{1}$').values_list('code', flat=True)
            level2_list = (super().get_queryset().filter(code__regex=r'^[0-9]{2}$').annotate(nu_code=F('code')/10).values_list('nu_code', flat=True), super().get_queryset().filter(code__regex=r'^[0-9]{2}$').values_list('code', flat=True))
            level3_list = (super().get_queryset().filter(code__regex=r'^[0-9]{4}$').annotate(nu_code=F('code')/100).values_list('nu_code', flat=True), super().get_queryset().filter(code__regex=r'^[0-9]{4}$').values_list('code', flat=True))
            level4_list = (super().get_queryset().filter(code__regex=r'^[0-9]{6}$').annotate(nu_code=F('code')/100).values_list('nu_code', flat=True), super().get_queryset().filter(code__regex=r'^[0-9]{6}$').values_list('code', flat=True))
            level5_list = (super().get_queryset().filter(code__regex=r'^[0-9]{8}$').annotate(nu_code=F('code')/100).values_list('nu_code', flat=True), super().get_queryset().filter(code__regex=r'^[0-9]{8}$').values_list('code', flat=True))
            level6_list = (super().get_queryset().filter(code__regex=r'^[0-9]{10}$').annotate(nu_code=F('code')/100).values_list('nu_code', flat=True), super().get_queryset().filter(code__regex=r'^[0-9]{10}$').values_list('code', flat=True))
            for obj in level1_list:
                if obj not in level2_list[0]:
                    chargeables.append(obj)
            for obj in level2_list[1]:
                if obj not in level3_list[0]:
                    chargeables.append(obj)
            for obj in level3_list[1]:
                if obj not in level4_list[0]:
                    chargeables.append(obj)
            for obj in level4_list[1]:
                if obj not in level5_list[0]:
                    chargeables.append(obj)
            for obj in level5_list[1]:
                if obj not in level6_list[0]:
                    chargeables.append(obj)
            for obj in level6_list[1]:
                chargeables.append(obj)
            return super().get_queryset().filter(code__in=chargeables).annotate(char_code=Cast('code', CharField())).order_by('char_code')
        except:
            return

class Account(BaseModel):
    
    code = models.PositiveBigIntegerField(
        primary_key=True,
        verbose_name='Código'
    )
    name = models.CharField(
        max_length=128,
        blank=True,
        verbose_name='Nombre'
    )

    class Meta:
        app_label = 'accounting'
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        permissions = [
            ('activate_account', 'Can activate account.'),
            ('view_balance', 'Can view balance.')
        ]

    objects = models.Manager()
    chargeables = Chargeables()

    @classmethod
    def account_name(cls, code):
        return cls.objects.get(code=code).name

    @classmethod
    def chargeable(cls, code):
        if not isinstance(code, int):
            code = int(code)
        return True if code in Account.chargeables.code_list() else False

    @property
    def levels(self):
        return Account_Structure.levels(self.code)

    @property
    def nature(self):
        return Account_Structure.nature(self.code)

    def __repr__(self) -> str:
        return f'<Acc: {self.code}>'
    
    def __str__(self) -> str:
        return str(self.code)