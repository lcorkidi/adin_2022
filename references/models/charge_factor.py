import datetime
from django.db import models
from django.db.models import Q

from adin.core.models import BaseModel
from adin.utils.data_check import errors_report

class Charge_Factor(BaseModel):

    name = models.CharField(
        max_length=63,
        primary_key=True
    )

    class Meta:
        app_label = 'references'
        verbose_name = 'Tasa Transacción'
        verbose_name_plural = 'Tasas Transacciones'
        permissions = [
            ('activate_charge_factor', 'Can activate charge factor.'),
            ('check_charge_factor', 'Can check charge factor.'),
        ]

    @classmethod
    def get_errors_report(cls, all=False):
        return errors_report(cls, all)

    # calculates the product int of the value with to the factor's attributes and nature
    def factored_value(self, accountable, date, value, nature):
        facdat = Factor_Data.objects.filter(factor=self).exclude(validity_date__gt=date).order_by('-validity_date')[0]
        if facdat.in_instance_attribute and facdat.in_instance_attribute != 'ZZZZ':
            fac = eval(f'accountable.subclass_obj().{facdat.in_instance_attribute}_id')
            facdat = Factor_Data.objects.filter(factor=fac).exclude(validity_date__gt=date).order_by('-validity_date')[0]
        if facdat.percentage > 0 and facdat.amount == 0:
            fac_value = int(value) * float(facdat.percentage / 100)
        elif facdat.percentage > 0 and facdat.amount > 0:
            fac_value = (int(value) + facdat.amount) * float(facdat.percentage / 100)
        elif facdat.percentage == 0 and facdat.amount > 0:
            fac_value = facdat.amount
        return round(fac_value * nature, 0)

    def get_obj_errors(self):
        errors = []
        # name (obligatory, length < 64)
        if not self.name:
            errors.append(90)
        elif len(self.name) > 63:
            errors.append(91)
        return errors

    def __repr__(self) -> str:
        return f'<Charge_Factor: {self.name}>'

    def __str__(self):
        return self.name

class Factor_Data(BaseModel):

    factor = models.ForeignKey(
        Charge_Factor,
        on_delete=models.PROTECT,
        related_name='datas',
        related_query_name='data',
        verbose_name='Tasa'
    )
    validity_date = models.DateField(
        verbose_name='Fecha Validez'
    )
    amount = models.PositiveIntegerField(
        verbose_name='Monto',
        default = 0
    )
    percentage = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        verbose_name='Porcentaje',
        default=100
    )
    in_instance_attribute = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        default=None,
        verbose_name='Atributo en Instancia'
    )

    class Meta:
        app_label = 'references'
        verbose_name = 'Datos Tasas'
        verbose_name_plural = 'Datos Tasas'
        constraints = [
            models.UniqueConstraint(fields=['factor', 'validity_date'], name='unique_factor_validity'),
        ]

    @classmethod
    def get_errors_report(cls, all=False):
        return errors_report(cls, all)

    def validity_end_date(self):
        qs = Factor_Data.objects.filter(validity_date__gt=self.validity_date, factor=self.factor)
        if qs.exists():
            return qs.order_by('-validity_date')[0].validity_date
        else:
            return datetime.date.today()

    def get_obj_errors(self):
        errors = []
        # factor (obligatory, related exists)
        if not self.factor:
            errors.append(92)
        if not Charge_Factor.objects.filter(pk=self.factor.pk).exists():
            errors.append(93)
        # validity_date (obligatory, date)
        if not self.validity_date:
            errors.append(94)
        if isinstance(self.validity_date, datetime.datetime):
            errors.append(95)
        # (ammount and percentage) or in_instance_attribute
        if (self.amount or self.percentage) and self.in_instance_attribute:
            errors.append(96)
        elif not self.in_instance_attribute:
            # ammount (0 or value)
            if not self.amount and self.amount != 0:
                errors.append(97)
            # percentage (o or 0 to 100)
            if not self.percentage and self.percentage != 0:
                errors.append(98)
            if self.percentage < 0 or self.percentage > 100:
                errors.append(99)
        elif self.in_instance_attribute:
            # in_instance_attribute (length < 16)
            if self.amount != 0 and self.percentage != 0:
                errors.append(100)
            if len(self.in_instance_attribute) > 15:
                errors.append(101)
        return errors

    def __repr__(self) -> str:
        return f'<Factor_Data: {self.factor.name}^{self.validity_date.strftime("%d-%m-%Y")}>'

    def __str__(self):
        return f'{self.factor.name}^{self.validity_date.strftime("%d-%m-%Y")}'

