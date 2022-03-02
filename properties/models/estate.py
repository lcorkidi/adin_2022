from django.db import models

class Estate(models.Model):

    national_number = models.PositiveIntegerField(
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
    appraisal = models.ManyToManyField(
        'references.Appraisal',
        related_name='estates',
        related_query_name='estate',
        verbose_name='Avaluo(s)'
    )
    total_area = models.FloatField(
        verbose_name='Área'
    )

    class Meta:
        app_label = 'properties'
        verbose_name = 'Predio'
        verbose_name_plural = 'Predios'

    def __str__(self) -> str:
        return f'<Estate: {self.address}>'

class Estate_Person(models.Model):

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

    def __str__(self) -> str:
        return f'<Estate_Person: {self.estate}-{self.person}>'
