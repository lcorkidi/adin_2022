from django.db import models

class Realty(models.Model):

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
    address = models.ForeignKey(
        'references.Address',
        on_delete=models.PROTECT,
        related_name='realties',
        related_query_name='realty',
        primary_key=True,
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

    def __str__(self) -> str:
        return f'<Realty: {self.code}>'

class Realty_Estate(models.Model):

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

    class Meta:
        app_label = 'properties'
        verbose_name = 'Predio Inmueble'
        verbose_name_plural = 'Predios Inmuebles'
        constraints = [
            models.UniqueConstraint(fields=['realty', 'estate'], name='unique_realty_estate'),
        ]

    def __str__(self) -> str:
        return f'<Realty_Estate: {self.realty}-{self.estate}>'
       