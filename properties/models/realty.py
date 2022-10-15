from django.db import models

from adin.core.models import BaseModel
from adin.utils.data_check import errors_report

class Realty(BaseModel):

    TYPE_CHOICE = [
        (0, 'Apartamento'),
        (1, 'Local'),
        (2, 'Oficina'),
        (3, 'Bodega'),
        (4, 'Parqueadero'),
        (5, 'Depósito'),
        (6, 'Casa'),
        (7, 'Lote'),
        (8, 'Finca'),
        (9, 'Apartaestudio')
    ]
    USE_CHOICE = [
        (0, 'Residencial'),
        (1, 'Comercial'),
        (2, 'Industrial')
    ]

    type = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICE,
        verbose_name='Tipo'
    )
    use = models.PositiveSmallIntegerField(
        choices=USE_CHOICE,
        verbose_name='Uso'
    )
    code = models.CharField(
        max_length=32,
        primary_key=True,
        verbose_name='Código'
    )
    address = models.ForeignKey(
        'references.Address',
        on_delete=models.PROTECT,
        related_name='realties',
        related_query_name='realty',
        verbose_name='Dirección'
    )
    estate = models.ManyToManyField(
        'properties.Estate',
        through='Realty_Estate',
        through_fields=('realty', 'estate'),
        related_name='realties',
        related_query_name='realty',
        verbose_name='Predio(s)'
    )
    total_area = models.FloatField(
        verbose_name='Área'
    )

    class Meta:
        app_label = 'properties'
        verbose_name = 'Inmueble'
        verbose_name_plural = 'Inmuebles'
        ordering = ['code']
        constraints = [
            models.UniqueConstraint(fields=['code', 'address'], name='realty_unique_code_address'),
        ]
        permissions = [
            ('activate_realty', 'Can activate realty.'),
            ('check_realty', 'Can check realty.'),
        ]

    @classmethod
    def get_errors_report(cls, all=False):
        return errors_report(cls, all)

    def is_vacant(self):
        for lease in self.leases_realties.all():
            if lease.is_active():
                return False
        return True

    def get_obj_errors(self):
        errors = []
        # type (oligatory, TYPE_CHOICE)
        if not self.type and self.type != 0:
            errors.append(37)
        elif self.type not in [x for x in range(0,len(self.TYPE_CHOICE))]:
            errors.append(43)
        # use (obligatory, USE_CHOICE)
        if not self.use and self.use != 0:
            errors.append(38)
        elif self.use not in [x for x in range(0,len(self.USE_CHOICE))]:
            errors.append(44)
        # code (obligatory, = address, length < 33)
        if not self.code:
            errors.append(39)
        else:
            if self.address and self.code != self.address.code:
                errors.append(126)
            if len(self.code) > 33:
                errors.append(127)
        # address (obligatory, active)
        if not self.address:
            errors.append(40)
        elif self.address.state == 0:
            errors.append(128)
        # estate (percentage = 100, active percentage active estate)
        if self.estate.exclude(realty_estate__state=0).count() == 0:
            errors.append(41)
        else:
            if self.estate.exclude(realty_estate__state=0).filter(state=0).exists():
                errors.append(112)
            if self.realty_estate_set.exclude(state=0).aggregate(models.Sum('percentage'))['percentage__sum'] != 100:
                errors.append(129)
        # total_area
        if not self.total_area or self.total_area <= 0:
            errors.append(42)
        return errors

    def __repr__(self) -> str:
        return f'<Realty: {self.address.pk}>'

    def __str__(self) -> str:
        return self.address.pk

class Realty_EstateFinderManager(models.Manager):
    def from_related(self, obj1, obj2):
        base_args = {}
        if isinstance(obj1, Realty):
            base_args['realty'] = obj1
            base_args['estate'] = obj2
        else:
            base_args['realty'] = obj2
            base_args['estate'] = obj1
        return self.get_queryset().get(**base_args)

    def get_queryset(self):
        return super().get_queryset()

class Realty_Estate(BaseModel):

    realty = models.ForeignKey(
        Realty,
        on_delete=models.PROTECT,
        verbose_name='Inmueble'
    )
    estate = models.ForeignKey(
        'properties.Estate',
        on_delete=models.PROTECT,
        verbose_name='Predio'
    )
    percentage = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        verbose_name='Participacion'
    )

    objects = models.Manager()
    find =  Realty_EstateFinderManager()

    class Meta:
        app_label = 'properties'
        verbose_name = 'Predio Inmueble'
        verbose_name_plural = 'Predios Inmuebles'
        constraints = [
            models.UniqueConstraint(fields=['realty', 'estate'], name='unique_realty_estate'),
        ]

    def __repr__(self) -> str:
        return f'<Realty_Estate: {self.realty.pk}_{self.estate.pk}>'

    def __str__(self) -> str:
        return f'{self.realty.pk}_{self.estate.pk}'
       