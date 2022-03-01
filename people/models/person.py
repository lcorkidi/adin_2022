from pyexpat import model
from django.db import models

class Person(models.Model):
    ID_TYPE_CHOICE = [
        (0, 'CC'),
        (1, 'NIT'),
        (2, 'TI'),
        (3, 'CE')
    ]
    TYPE_CHOICE = [
        (0, 'Natural'),
        (1, 'Legal')
    ]
    id_number = models.PositiveSmallIntegerField(
        primary_key=True,
        verbose_name='Número DI'
    )
    id_type = models.PositiveSmallIntegerField(
        choices=ID_TYPE_CHOICE,
        verbose_name='Tipo DI'
    )
    type = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICE,
        verbose_name='Tipo Persona'
    )
    name = models.CharField(
        max_length=64,
        verbose_name='Nombre(s)'
    )
    phone = models.ManyToManyField(
        'phones.Phone',
        through='Person_Phone',
        through_fields=('person', 'phone'),
        related_name='phones',
        related_query_name='phone',
        verbose_name='Teléfono'
    )

    class Meta:
        app_label = 'people'

    def __str__(self) -> str:
        if self.person_type == 0:
            return Person_Natural.objects.get(pk=self.pk)
        elif self.person_type == 1:
            return Person_Legal.objects.get(pk=self.pk)

class Person_Natural(Person):
    last_name = models.CharField(
        max_length=64,
        verbose_name='Apellido(s)'
    )

    def __str__(self) -> str:
        return f'{self.last_name}, {self.name}'

class Person_Legal(Person):
    LEGAL_TYPE_CHOICE = [
        (0, 'S.A.'),
        (1, 'S.A.S'),
        (2, 'LTDA.'),
        (3, 'E.U.'),
        (4, '& CIA.'),
        (5, 'S. en C.') 
    ]
    legal_type = models.PositiveSmallIntegerField(
        choices=LEGAL_TYPE_CHOICE,
        verbose_name='Tipo de Sociedad'
    )
    
    def __str__(self) -> str:
        return f'{self.name} {self.get_person_legal_type_display()}'

class Person_Phone(models.Model):
    PHONE_USE_CHOICE = [
        (0, 'Personal'),
        (1, 'Residencia'),
        (2, 'Auxiliar Administrativo'),
        (3, 'Auxiliar Contable')
    ]
    person = models.ForeignKey(
        Person,
        on_delete=models.PROTECT,
        verbose_name='Persona'
    )
    phone = models.ForeignKey(
        'phones.Phone',
        on_delete=models.PROTECT,
        verbose_name='Teléfono'
    )
    use = models.PositiveSmallIntegerField(
        choices=PHONE_USE_CHOICE,
        verbose_name='Tipo'
    )

    def __str__(self) -> str:
        return f'{self.get_use_disply()} - {self.person}'