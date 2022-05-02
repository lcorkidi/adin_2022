from django.db import models
from adin.core.models import BaseModel

class Phone(BaseModel):

    TYPE_CHOICE = [
        (0, 'Fijo'),
        (1, 'Movil')
    ]

    code = models.CharField(
        max_length=16,
        primary_key=True,
        verbose_name='Código'
    )
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
        ordering = ['code']
        constraints = [
            models.UniqueConstraint(fields=['country', 'region', 'number'], name='unique_country_region_number'),
        ]
        permissions = [
            ('activate_phone', 'Can activate phone.'),
        ]

    def __repr__(self) -> str:
        return f'<Phone: {self.code}>'

    def __str__(self) -> str:
        return self.code
