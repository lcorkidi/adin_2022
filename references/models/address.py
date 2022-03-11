from django.db import models
from adin.core.models import BaseModel

from references.utils import addresslong

class Address(BaseModel):

    STREET_TYPE_CHOICE = [
        (0, 'Avenida'),
        (1, 'Calle'),
        (2, 'Carrera'),
        (3, 'Diagonal'),
        (4, 'Transversal'),
        (5, 'Circunvalar'),
        (6, 'Circular'),
        (7, 'Autopista')
    ]
    LETTER_CHOICE = [
        (0, 'A'),
        (1, 'B'),
        (2, 'C'),
        (3, 'D'),
        (4, 'E'),
        (5, 'F'),
        (6, 'G'),
        (7, 'H'),
        (8, 'I'),
        (9, 'J'),
        (10, 'K'),
        (11, 'L'),
        (12, 'M'),
        (13, 'M'),
        (14, 'O'),
        (15, 'P'),
        (16, 'Q'),
        (17, 'R'),
        (18, 'S'),
        (19, 'T'),
        (20, 'U'),
        (21, 'V'),
        (22, 'W'),
        (23, 'X'),
        (24, 'Y'),
        (25, 'Z'),
        (26, 'A1'),
        (27, 'B1')
    ]
    COORDINATE_CHOICE = [
        (0, 'Norte'),
        (1, 'Sur'),
        (2, 'Este'),
        (3, 'Oeste'),
        (4, 'Centro')
    ]
    INTERIOR_GROUP_TYPE_CHOICE = [
        (0, 'Bloque'),
        (1, 'Torre'),
        (2, 'Edificio')
    ]
    INTERIOR_TYPE_CHOICE = [
        (0, 'Apartamento'),
        (1, 'Local'),
        (2, 'Oficina'),
        (3, 'Bodega'),
        (4, 'Parqueadero'),
        (5, 'Depósito'),
        (6, 'Interior'),
        (7, 'Casa'),
        (8, 'Lote'),
        (9, 'Finca'),
        (10, 'Apartaestudio')
    ]

    code = models.CharField(
        primary_key=True,
        max_length=32,
        verbose_name='Código'
    )
    country = models.CharField(
        max_length=32,
        verbose_name='País'
    )
    region = models.CharField(
        max_length=32,
        verbose_name='Departamento'
    )
    city = models.CharField(
        max_length=32,
        verbose_name='Ciudad'
    )
    street_type = models.PositiveSmallIntegerField(
        choices=STREET_TYPE_CHOICE,
        verbose_name='Vía'
    )
    street_number = models.PositiveSmallIntegerField(
        verbose_name='Número Vía'
    )
    street_letter = models.PositiveSmallIntegerField(
        choices=LETTER_CHOICE,
        verbose_name='Letra Vía',
        blank=True,
        null=True,
        default=None
    )
    street_bis = models.BooleanField(
        verbose_name='Bis Vía',
        blank=True,
        null=True,
        default=None        
    )
    street_bis_complement = models.PositiveSmallIntegerField(
        choices=LETTER_CHOICE,
        verbose_name='Letra Bis Vía',
        blank=True,
        null=True,
        default=None
    )
    street_coordinate = models.PositiveSmallIntegerField(
        choices=COORDINATE_CHOICE,
        verbose_name='Cardinalidad Vía',
        blank=True,
        null=True,
        default=None
    )
    numeral_number = models.PositiveSmallIntegerField(
        verbose_name='Número',
    )
    numeral_letter = models.PositiveSmallIntegerField(
        choices=LETTER_CHOICE,
        verbose_name='Letra Número',
        blank=True,
        null=True,
        default=None
    )
    numeral_bis = models.BooleanField(
        verbose_name='Bis Número',
        blank=True,
        null=True,
        default=None        
    )
    numeral_bis_complement = models.PositiveSmallIntegerField(
        choices=LETTER_CHOICE,
        verbose_name='Letra Bis Número',
        blank=True,
        null=True,
        default=None
    )
    numeral_coordinate = models.PositiveSmallIntegerField(
        choices=COORDINATE_CHOICE,
        verbose_name='Cardinalidad Número',
        blank=True,
        null=True,
        default=None
    )
    height_number = models.PositiveSmallIntegerField(
        verbose_name='Altura Nomenclatura'
    )
    interior_group_type = models.PositiveSmallIntegerField(
        choices=INTERIOR_GROUP_TYPE_CHOICE,
        verbose_name='Interior Grupo Tipo',
        blank=True,
        null=True,
        default=None
    )
    interior_group_code = models.CharField(
        max_length=6,
        verbose_name='Interior Grupo Código',
        blank=True,
        null=True,
        default=None
    )
    interior_type = models.PositiveSmallIntegerField(
        choices=INTERIOR_TYPE_CHOICE,
        verbose_name='Interior Tipo',
        blank=True,
        null=True,
        default=None
    )
    interior_code = models.CharField(
        max_length=6,
        verbose_name='Interior Código',
        blank=True,
        null=True,
        default=None
    )

    class Meta:
        app_label = 'references'
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'

    def __repr__(self) -> str:
        return f'<Addresss: {self.code}, {self.city}>'

    def __str__(self) -> str:
        return addresslong(self)