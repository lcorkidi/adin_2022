from datetime import datetime
from django.db import models

from adin.core.models import BaseModel
from adin.utils.data_check import errors_report

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
        permissions = [
            ('activate_estate', 'Can activate estate.'),
        ]

    @classmethod
    def get_errors_report(cls, all=False):
        return errors_report(cls, all)

    def get_obj_errors(self):
        errors = []
        # national_number (obligatory, length 30)
        if not self.national_number:
            errors.append(32)
        elif len(self.national_number) != 30:
            errors.append(109)
        # address (obligatory, unique with national_number, active)
        if not self.address:
            errors.append(33)
        else:
            if Estate.objects.exclude(national_number=self.national_number, address=self.address).filter(national_number=self.national_number).exists():
                errors.append(110)
            if Estate.objects.exclude(national_number=self.national_number, address=self.address).filter(address=self.address).exists():
                errors.append(111)
            if self.address.state == 0:
                errors.append(125)
        # owner (percentage = 100, active percentage active person)
        if self.estate_person_set.exclude(state=0).count() == 0:
            errors.append(34)
        else:
            if self.estate_person_set.exclude(state=0).filter(person__state=0).exists():
                errors.append(112)
            if self.estate_person_set.exclude(state=0).aggregate(models.Sum('percentage'))['percentage__sum'] != 100:
                errors.append(36)
        # total_area (obligatory, positive)
        if not self.total_area or self.total_area <= 0:
            errors.append(35)
        return errors

    def __repr__(self) -> str:
        return f'<Estate: {self.address.pk}>'

    def __str__(self) -> str:
        return self.address.pk

class Estate_PersonFinderManager(models.Manager):
    def from_related(self, obj1, obj2):
        base_args = {}
        if isinstance(obj1, Estate):
            base_args['estate'] = obj1
            base_args['person'] = obj2
        else:
            base_args['estate'] = obj2
            base_args['person'] = obj1
        return self.get_queryset().get(**base_args)

    def get_queryset(self):
        return super().get_queryset()

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

    objects = models.Manager()
    find =  Estate_PersonFinderManager()

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
        verbose_name='Predio'
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

    @classmethod
    def get_errors_report(cls, all=False):
        return errors_report(cls, all)

    def get_obj_errors(self):
        errors = []
        # estate (obligatory, active)
        if not self.estate:
            errors.append(113)
        if self.estate.state == 0:
            errors.append(114)
        # type (obligatory, TYPE_CHOICE)
        if not self.type and self.type != 0:
            errors.append(115)
        elif self.type not in [x for x in range(0,len(self.TYPE_CHOICE))]:
            errors.append(116)
        # date (obligatory, date)
        if not self.date:
            errors.append(117)
        if isinstance(self.date, datetime):
            errors.append(118)
        # value (obligatory, positive integer)
        if not self.value:
            errors.append(119)
        elif not self.value > 0 and not isinstance(self.value, int):
            errors.append(120)
        return errors

    def __repr__(self) -> str:
        return f'Estate_Appraisal: {self.get_type_display()}_{self.date}_{self.value}>'

    def __str__(self) -> str:
        return f'{self.get_type_display()}_{self.date}_{self.value}'