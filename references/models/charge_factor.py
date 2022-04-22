from django.db import models
from django.db.models import Q

from adin.core.models import BaseModel

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
        ]

    # calculates the product int of the value with to the factor's attributes and nature
    def factored_value(self, accountable, date, value, nature):
        facdat = Factor_Data.objects.filter(factor=self).exclude(validity_date__gt=date).order_by('-validity_date')[0]
        if facdat.in_instance_attribute and facdat.in_instance_attribute != 'ZZZZ':
            fac = eval(f'accountable.{facdat.in_instance_attribute}_id')
            facdat = Factor_Data.objects.filter(factor=fac).exclude(validity_date__gt=date).order_by('-validity_date')[0]
        if facdat.percentage > 0 and facdat.amount == 0:
            fac_value = int(value) * float(facdat.percentage / 100)
        elif facdat.percentage > 0 and facdat.amount > 0:
            fac_value = (int(value) + facdat.amount) * float(facdat.percentage / 100)
        elif facdat.percentage == 0 and facdat.amount > 0:
            fac_value = facdat.amount
        return round(fac_value * nature, 0)

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
            models.CheckConstraint(check=Q(percentage__gte=0) & Q(percentage__lte=100), name='facdat_percentage_gte_0_and_lte_100'),
        ]

    def __repr__(self) -> str:
        return f'<Factor_Data: {self.factor.name}^{self.validity_date.strftime("%d-%m-%Y")}>'

    def __str__(self):
        return f'{self.factor.name}^{self.validity_date.strftime("%d-%m-%Y")}'

