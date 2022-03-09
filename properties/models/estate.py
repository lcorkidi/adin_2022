from django.db import models
from adin.core.models import BaseModel

class Estate(BaseModel):

    national_number_1 = models.PositiveBigIntegerField(
        verbose_name='Número Predial Nacional'
    )
    national_number_2 = models.PositiveBigIntegerField(
        verbose_name='Número Predial Nacional'
    )
    national_number_3 = models.PositiveBigIntegerField(
        verbose_name='Número Predial Nacional'
    )
    address = models.ForeignKey(
        'references.Address',
        on_delete=models.PROTECT,
        related_name='estates',
        related_query_name='estate',
        primary_key=True,
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
