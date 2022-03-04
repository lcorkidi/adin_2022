from django.db import models

class Phone(models.Model):

    TYPE_CHOICE = [
        (0, 'Fijo'),
        (1, 'Movil')
    ]

    type = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICE,
        verbose_name='Tipo'
    )
    country = models.PositiveSmallIntegerField(
        default=57,
        verbose_name='País'
    )
    region = models.PositiveSmallIntegerField(
        verbose_name='Región',
        blank=True,
        null=True,
        default=None
    )
    number = models.PositiveIntegerField(
        verbose_name='Número'
    )

    class Meta:
        app_label = 'references'
        verbose_name = 'Teléfono'
        verbose_name_plural = 'Teléfonos'
        constraints = [
            models.UniqueConstraint(fields=['country', 'region', 'number'], name='unique_country_region_number'),
        ]

    def __repr__(self) -> str:
        return f'<Phone: +{self.country}{" " + self.region if self.region != None else ""} {self.number}>'

    def __str__(self) -> str:
        return f'+{self.country}{" " + self.region if self.region != None else ""} {self.number}'