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
        verbose_name = 'Factor Movimiento'
        verbose_name_plural = 'Factores Moviminetos'
        permissions = [
            ('charge_factor', 'Can activate charge factor.'),
        ]

    # # applies current factor to reg_regtem.value according to the factor's attributes, factors for nature and rounds to int
    # def get_fac_value_from_regtem(self, ref_regtem, ref_chatem):
    #     facdat = Factor_Data.objects.filter(factor=self).exclude(validity_date__gt=ref_regtem.date).order_by('-validity_date')[0]
    #     if facdat.in_instance_attribute:
    #         fac = eval(f'ref_regtem.refbas.{facdat.in_instance_attribute}_id')
    #         facdat = Factor_Data.objects.filter(factor=fac).exclude(validity_date__gt=ref_regtem.date).order_by('-validity_date')[0]
    #     if facdat.percentage > 0 and facdat.amount == 0:
    #         fac_value = int(ref_regtem.value) * float(facdat.percentage / 100)
    #     elif facdat.percentage > 0 and facdat.amount > 0:
    #         fac_value = (int(ref_regtem.value) + facdat.amount) * float(facdat.percentage / 100)
    #     elif facdat.percentage == 0 and facdat.amount > 0:
    #         fac_value = facdat.amount
    #     return round(fac_value * ref_chatem.nature, 0)

    def __repr__(self) -> str:
        return f'<Charge_Factor: {self.name}>'

    def __str__(self):
        return self.name

class Factor_Data(BaseModel):

    factor = models.ForeignKey(
        Charge_Factor,
        on_delete=models.PROTECT,
        related_name='datas',
        related_query_name='data'
    )
    validity_date = models.DateField(
        verbose_name='Fecha Validez'
    )
    amount = models.PositiveIntegerField(
        verbose_name='Monto'
    )
    percentage = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        verbose_name='Porcentaje'
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
        verbose_name = 'Datos Factor'
        verbose_name_plural = 'Datos Factores'
        constraints = [
            models.UniqueConstraint(fields=['factor', 'validity_date'], name='unique_factor_validity'),
            models.CheckConstraint(check=Q(percentage__gte=0) & Q(percentage__lte=100), name='facdat_percentage_gte_0_and_lte_100'),
        ]

    def __repr__(self) -> str:
        return f'<Factor_Data: {self.factor.name}^{self.validity_date.strftime("%d-%m-%Y")}>'

    def __str__(self):
        return f'{self.factor.name}^{self.validity_date.strftime("%d-%m-%Y")}'

