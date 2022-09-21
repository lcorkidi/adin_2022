from django.db import models

from adin.core.models import BaseModel
from references.utils import address2code, addresslong
from adin.utils.data_check import errors_report

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
        (10, 'Apartaestudio'),
        (11, 'Piso')
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
        ordering = ['code']
        permissions = [
            ('address', 'Can activate address.'),
        ]

    @classmethod
    def get_errors_report(cls, all=False):
        return errors_report(cls, all)

    def get_obj_errors(self):
        errors = []
        # code (obligatory, function of other attributes, length < 33)
        if not self.code:
            errors.append(45)
        elif self.code != address2code(self):
            errors.append(46) 
        elif len(self.code) > 32:
            errors.append(47)
        # country (obligatory, length < 33)
        if not self.country:
            errors.append(48)
        elif len(self.country) > 32:
            errors.append(49)
        # region (obligatory, length < 33)
        if not self.region:
            errors.append(50)
        elif len(self.region) > 32:
            errors.append(51)
        # city (obligatory, length < 33)
        if not self.city:
            errors.append(52)
        elif len(self.city) > 32:
            errors.append(53)
        # street_type (obligatory, must be STREET_TYPE_CHOICE)
        if not self.street_type and self.street_type != 0:
            errors.append(54)
        elif self.street_type not in [x for x in range(0,len(self.STREET_TYPE_CHOICE))]:
            errors.append(55)
        # street_number (obligatory, positive integer)
        if not self.street_number:
            errors.append(56)
        elif not self.street_number > 0 and not isinstance(self.street_number, int):
            errors.append(57)
        # street_letter (must be LETTER_CHOICE)
        if (self.street_letter or self.street_letter == 0) and self.street_letter not in [x for x in range(0,len(self.LETTER_CHOICE))]:
            errors.append(58)
        # street_bis (must be bool)
        if self.street_bis:
            if not isinstance(self.street_bis, bool):
                errors.append(59)
            else:
                # street_bis_complement (only if street_bis, must be LETTER_CHOICE)
                if (self.street_bis_complement or self.street_bis_complement == 0) and self.street_bis_complement not in [x for x in range(0,len(self.LETTER_CHOICE))]:
                    errors.append(68)
        elif self.street_bis_complement or self.street_bis_complement == 0:
            errors.append(72)
        # street_coordinate (must be COORDINATE_CHOICE)
        if (self.street_coordinate or self.street_coordinate == 0) and self.street_coordinate not in [x for x in range(0,len(self.COORDINATE_CHOICE))]:
            errors.append(62)
        # numeral_number (obligatory, positive integer)
        if not self.numeral_number:
            errors.append(63)
        elif not self.numeral_number > 0 and not isinstance(self.numeral_number, int):
            errors.append(64)
        # numeral_letter (must be LETTER_CHOICE)
        if (self.numeral_letter or self.numeral_letter == 0) and self.numeral_letter not in [x for x in range(0,len(self.LETTER_CHOICE))]:
            errors.append(65)
        # numeral_bis (must be bool)
        if self.numeral_bis:
            if not isinstance(self.numeral_bis, bool):
                errors.append(66)
            else:
                # numeral_bis_complement (only if numeral_bis, must be LETTER_CHOICE)
                if (self.numeral_bis_complement or self.numeral_bis_complement == 0) and self.numeral_bis_complement not in [x for x in range(0,len(self.LETTER_CHOICE))]:
                    errors.append(68)
        elif self.numeral_bis_complement or self.numeral_bis_complement == 0:
            errors.append(73)
        # numeral_coordinate (must be COORDINATE_CHOICE)
        if (self.numeral_coordinate or self.numeral_coordinate == 0) and self.numeral_coordinate not in [x for x in range(0,len(self.COORDINATE_CHOICE))]:
            errors.append(69)
        # height_number (obligatory, positive integer)
        if not self.height_number:
            errors.append(70)
        elif not self.height_number > 0 and not isinstance(self.height_number, int):
            errors.append(71)
        # interior_type (must be INTERIOR_TYPE_CHOICE)
        if (self.interior_type or self.interior_type == 0):
            if self.interior_type not in [x for x in range(0,len(self.INTERIOR_TYPE_CHOICE))]:
                errors.append(74)
            # interior_code (only if interior_type, length < 7)
            if not self.interior_code:
                errors.append(75)
            elif len(self.interior_code) > 7:
                errors.append(76)
            else:
                # interior_group_type (only if interior_type and interior_code, must be INTERIOR_GROUP_TYPE_CHOICE)
                if (self.interior_group_type or self.interior_group_type == 0):
                    if self.interior_group_type not in [x for x in range(0,len(self.INTERIOR_TYPE_CHOICE))]:
                        errors.append(78)
                    # interior_group_code (only if interior_group_type, length < 7)
                    if not self.interior_group_code:
                        errors.append(79)
                    elif len(self.interior_group_code) > 7:
                        errors.append(80)
                elif (self.interior_group_code or self.interior_group_code == 0):
                    errors.append(81)
        else:
            if (self.interior_code or self.interior_code == 0):
                errors.append(77)
                if (self.interior_group_type or self.interior_group_type == 0):
                    errors.append(82)
                if (self.interior_group_code or self.interior_group_code == 0):
                    errors.append(83)
            if (self.interior_group_type or self.interior_group_type == 0):
                errors.append(84)
            if (self.interior_group_code or self.interior_group_code == 0):
                errors.append(85)
        return errors

    def __repr__(self) -> str:
        return f'<Addresss: {self.code}, {self.city}>'

    def __str__(self) -> str:
        return addresslong(self)