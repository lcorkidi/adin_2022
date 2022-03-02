from pyexpat import model
from statistics import mode
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
        'references.Phone',
        through='Person_Phone',
        through_fields=('person', 'phone'),
        related_name='people',
        related_query_name='person',
        verbose_name='Teléfono'
    )
    address = models.ManyToManyField(
        'references.Address',
        through='Person_Address',
        through_fields=('person', 'address'),
        related_name='people',
        related_query_name='person',
        verbose_name='Dirección'
    )
    email = models.ManyToManyField(
        'references.Email',
        through='Person_Email',
        through_fields=('person', 'email'),
        related_name='people',
        related_query_name='person',
        verbose_name='Correo Electrónico'
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

    class Meta:
        app_label = 'people'

    def __str__(self) -> str:
        return f'<Person_Natural: {self.last_name}, {self.name}>'

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

    class Meta:
        app_label = 'people'
    
    def __str__(self) -> str:
        return f'<Person_Legal: {self.name} {self.get_person_legal_type_display()}>'

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
        'references.Phone',
        on_delete=models.PROTECT,
        verbose_name='Teléfono'
    )
    use = models.PositiveSmallIntegerField(
        choices=PHONE_USE_CHOICE,
        verbose_name='Uso'
    )

    class Meta:
        app_label = 'people'

    def __str__(self) -> str:
        return f'<Phone: {self.get_use_disply()}-{self.person}>'


class Person_Address(models.Model):

    ADDRESS_USE_CHOICE = [
        (0, 'Residencia'),
        (1, 'Trabajo'),
        (2, 'Planta'),
        (3, 'Administración'),
        (4, 'Punto de Venta')
    ]

    person = models.ForeignKey(
        Person,
        on_delete=models.PROTECT,
        verbose_name='Persona'
    )
    address = models.ForeignKey(
        'references.Address',
        on_delete=models.PROTECT,
        verbose_name='Dirección'
    )
    use = models.PositiveSmallIntegerField(
        choices=ADDRESS_USE_CHOICE,
        verbose_name='Uso'
    )

    class Meta:
        app_label = 'people'

    def __str__(self) -> str:
        return f'<Address: {self.get_use_disply()}-{self.person}>'

class Person_Email(models.Model):

    EMAIL_USE_CHOICE = [
        (0, 'Principal'),
        (1, 'Adicional')
    ]

    person = models.ForeignKey(
        Person,
        on_delete=models.PROTECT,
        verbose_name='Persona'
    )
    email = models.ForeignKey(
        'references.Email',
        on_delete=models.PROTECT,
        verbose_name='Correo Electrónico'
    )
    use = models.PositiveSmallIntegerField(
        choices=EMAIL_USE_CHOICE,
        verbose_name='Uso'
    )

    class Meta:
        app_label = 'people'

    def __str__(self) -> str:
        return f'<Email: {self.get_use_disply()}-{self.person}>'
