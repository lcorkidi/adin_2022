from django.db import models
from adin.core.models import BaseModel

class Estate(BaseModel):

    national_number = models.CharField(
        max_length=30,
        primary_key=True,
        verbose_name='Número Predial Nacional'
    )
    address = models.ForeignKey(
        'references.Address',
        on_delete=models.PROTECT,
        related_name='estates',
        related_query_name='estate',
        verbose_name='Dirección'
    )
    owner = models.ManyToManyField(
        'people.Person',
        through='Estate_Person',
        through_fields=('estate', 'person'),
        related_name='estates',
        related_query_name='estate',
        verbose_name='Propietario(s)'
    )
    total_area = models.FloatField(
        verbose_name='Área',
        blank=True,
        null=True,
        default=None
    )

    class Meta:
        app_label = 'properties'
        verbose_name = 'Predio'
        verbose_name_plural = 'Predios'
        constraints = [
            models.UniqueConstraint(fields=['national_number', 'address'], name='unique_code_address'),
        ]

    def __repr__(self) -> str:
        return f'<Estate: {self.address.pk}>'

    def __str__(self) -> str:
        return self.address.pk

class Estate_Person(BaseModel):

    estate = models.ForeignKey(
        Estate,
        on_delete=models.PROTECT,
        verbose_name='Predio'
    )
    person = models.ForeignKey(
        'people.Person',
        on_delete=models.PROTECT,
        verbose_name='Persona'
    )
    percentage = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        verbose_name='Participacion'
    )

    class Meta:
        app_label = 'properties'
        verbose_name = 'Propietario Predio'
        verbose_name_plural = 'Propietarios Predios'
        constraints = [
            models.UniqueConstraint(fields=['estate', 'person'], name='unique_estate_person'),
        ]

    def __repr__(self) -> str:
        return f'<Estate_Person: {self.estate.pk}_{self.person.complete_name}>'

    def __str__(self) -> str:
        return f'{self.estate.pk}_{self.person.complete_name}'

class Estate_Appraisal(BaseModel):

    TYPE_CHOICE = [
        (0, 'Catastral'),
        (1, 'Comercial')
    ]

    estate = models.ForeignKey(
        'properties.Estate',
        on_delete=models.CASCADE,
        related_name='estates_appraisals',
        related_query_name='estate_appraisal',
        verbose_name='Avaluo Predio'
    )
    type = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICE,
        verbose_name='Tipo'
    )
    date = models.DateField(
        verbose_name='Fecha'
    )
    value = models.PositiveBigIntegerField(
        verbose_name='Valor'
    )

    class Meta:
        app_label = 'properties'
        verbose_name = 'Avaluo Predio'
        verbose_name_plural = 'Avaluos Predios'

    def __repr__(self) -> str:
        return f'Estate_Appraisal: {self.get_type_display()}_{self.date}_{self.value}>'

    def __str__(self) -> str:
        return f'{self.get_type_display()}_{self.date}_{self.value}'