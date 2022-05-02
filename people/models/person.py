from django.db import models
from adin.core.models import BaseModel
from references.models import Address, E_Mail, Phone

class Person(BaseModel):

    ID_TYPE_CHOICE = [
        (0, 'CC'),
        (1, 'NIT'),
        (2, 'TI'),
        (3, 'CE')
    ]
    TYPE_CHOICE = [
        (0, 'Natural'),
        (1, 'Jurídica')
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
    complete_name = models.CharField(
        max_length=128,
        verbose_name='Nombre Completo'
    )
    phone = models.ManyToManyField(
        'references.Phone',
        through='Person_Phone',
        through_fields=('person', 'phone'),
        related_name='people',
        related_query_name='person',
        blank=True,
        verbose_name='Teléfono'
    )
    address = models.ManyToManyField(
        'references.Address',
        through='Person_Address',
        through_fields=('person', 'address'),
        related_name='people',
        related_query_name='person',
        blank=True,
        verbose_name='Dirección'
    )
    e_mail = models.ManyToManyField(
        'references.E_Mail',
        through='Person_E_Mail',
        through_fields=('person', 'e_mail'),
        related_name='people',
        related_query_name='person',
        blank=True,
        verbose_name='Correo Electrónico'
    )

    class Meta:
        app_label = 'people'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['complete_name']
        permissions = [
            ('activate_person', 'Can activate person.'),
        ]

    def __repr__(self) -> str:
        return f'<Person: {self.complete_name}>'

    def __str__(self) -> str:
        return self.complete_name

class Person_Natural(Person):

    last_name = models.CharField(
        max_length=64,
        verbose_name='Apellido(s)'
    )

    class Meta:
        app_label = 'people'
        verbose_name = 'Persona Natural'
        verbose_name_plural = 'Personas Naturales'
        ordering = ['complete_name']

    def __repr__(self) -> str:
        return f'<Person_Natural: {self.complete_name}>'

    def __str__(self) -> str:
        return self.complete_name

class Person_Legal(Person):

    LEGAL_TYPE_CHOICE = [
        (0, 'S.A.'),
        (1, 'S.A.S.'),
        (2, 'LTDA.'),
        (3, 'E.U.'),
        (4, '& CIA.'),
        (5, 'S. en C.') 
    ]

    legal_type = models.PositiveSmallIntegerField(
        choices=LEGAL_TYPE_CHOICE,
        verbose_name='Tipo de Sociedad'
    )
    staff = models.ManyToManyField(
        'people.Person_Natural',
        through='Person_Legal_Person_Natural',
        through_fields=('person_legal', 'person_natural'),
        related_name='people_legal',
        related_query_name='person_legal',
        blank=True,
        verbose_name='Personal'
    )

    class Meta:
        app_label = 'people'
        verbose_name = 'Persona Jurídica'
        verbose_name_plural = 'Personas Jurídicas'
        ordering = ['complete_name']

    def __repr__(self) -> str:
        return f'<Person_Legal: {self.complete_name}>'
    
    def __str__(self) -> str:
        return self.complete_name

class Person_PhoneFinderManager(models.Manager):
    def from_related(self, obj1, obj2):
        base_args = {}
        if isinstance(obj1, Phone):
            base_args['phone'] = obj1
            base_args['person'] = obj2
        else:
            base_args['phone'] = obj2
            base_args['person'] = obj1
        return self.get_queryset().get(**base_args)

    def get_queryset(self):
        return super().get_queryset()

class Person_Phone(BaseModel):

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

    objects = models.Manager()
    find = Person_PhoneFinderManager()

    class Meta:
        app_label = 'people'
        verbose_name = 'Teléfono Persona'
        verbose_name_plural = 'Teléfonos Personas'
        constraints = [
            models.UniqueConstraint(fields=['person', 'phone'], name='unique_person_phone'),
        ]

    def __repr__(self) -> str:
        return f'<Person_Phone: {self.get_use_display()}_{self.person.complete_name}>'

    def __str__(self) -> str:
        return f'{self.get_use_display()}_{self.person.complete_name}'

class Person_AddressFinderManager(models.Manager):
    def from_related(self, obj1, obj2):
        base_args = {}
        if isinstance(obj1, Address):
            base_args['address'] = obj1
            base_args['person'] = obj2
        else:
            base_args['address'] = obj2
            base_args['person'] = obj1
        return self.get_queryset().get(**base_args)

    def get_queryset(self):
        return super().get_queryset()

class Person_Address(BaseModel):

    ADDRESS_USE_CHOICE = [
        (0, 'Residencia'),
        (1, 'Trabajo'),
        (2, 'Planta'),
        (3, 'Administración'),
        (4, 'Punto de Venta'),
        (5, 'Establecimiento de Comercio')
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

    objects = models.Manager()
    find = Person_AddressFinderManager()

    class Meta:
        app_label = 'people'
        verbose_name = 'Dirección Persona'
        verbose_name_plural = 'Direcciones Personas'
        constraints = [
            models.UniqueConstraint(fields=['person', 'address'], name='unique_person_address'),
        ]

    def __repr__(self) -> str:
        return f'<Person_Address: {self.get_use_display()}_{self.person.complete_name}>'

    def __str__(self) -> str:
        return f'{self.get_use_display()}_{self.person.complete_name}'

class Person_E_MailFinderManager(models.Manager):
    def from_related(self, obj1, obj2):
        base_args = {}
        if isinstance(obj1, E_Mail):
            base_args['e_mail'] = obj1
            base_args['person'] = obj2
        else:
            base_args['e_mail'] = obj2
            base_args['person'] = obj1
        return self.get_queryset().get(**base_args)

    def get_queryset(self):
        return super().get_queryset()

class Person_E_Mail(BaseModel):

    EMAIL_USE_CHOICE = [
        (0, 'Principal'),
        (1, 'Adicional')
    ]

    person = models.ForeignKey(
        Person,
        on_delete=models.PROTECT,
        verbose_name='Persona'
    )
    e_mail = models.ForeignKey(
        'references.E_Mail',
        on_delete=models.PROTECT,
        verbose_name='Correo Electrónico'
    )
    use = models.PositiveSmallIntegerField(
        choices=EMAIL_USE_CHOICE,
        verbose_name='Uso'
    )

    objects = models.Manager()
    find = Person_E_MailFinderManager()

    class Meta:
        app_label = 'people'
        verbose_name = 'Correo Electrónico Personas'
        verbose_name_plural = 'Correos Electrónicos Personas'
        constraints = [
            models.UniqueConstraint(fields=['person', 'e_mail'], name='unique_person_e_mail'),
        ]

    def __repr__(self) -> str:
        return f'<Person_E_Mail: {self.get_use_display()}_{self.person.complete_name}>'

    def __str__(self) -> str:
        return f'{self.get_use_display()}_{self.person.complete_name}'

class Person_Legal_Person_NaturalFinderManager(models.Manager):
    def from_related(self, obj1, obj2):
        base_args = {}
        if isinstance(obj1, Person_Legal):
            base_args['person_legal'] = obj1
            base_args['person_natural'] = obj2
        else:
            base_args['person_legal'] = obj2
            base_args['person_natural'] = obj1
        return self.get_queryset().get(**base_args)

    def get_queryset(self):
        return super().get_queryset()

class Person_Legal_Person_Natural(BaseModel):
    APPOINTMENT_CHOICE = [
        (0, 'Representate Legal'),
        (1, 'Gerente General'),
        (2, 'Suplente'),
        (3, 'Auxiliar Administración'),
        (4, 'Auxialr Contabilidad'),
        (5, 'Supervisor Planta'),
        (6, 'Socio')
    ]

    person_legal = models.ForeignKey(
        Person_Legal,
        on_delete=models.PROTECT,
        verbose_name='Empresa'
    )
    person_natural = models.ForeignKey(
        Person_Natural,
        on_delete=models.PROTECT,
        verbose_name='Personal'
    )
    appointment = models.PositiveSmallIntegerField(
        choices=APPOINTMENT_CHOICE,
        verbose_name='Cargo'
    )

    objects = models.Manager()
    find = Person_Legal_Person_NaturalFinderManager()

    class Meta:
        app_label = 'people'
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'
        constraints = [
            models.UniqueConstraint(fields=['person_legal', 'person_natural'], name='unique_person_legal_person_natural'),
        ]

    def __repr__(self) -> str:
        return f'<Person_Legal_Person_Natural: {self.get_appointment_display()}_{self.person_legal.complete_name}>'

    def __str__(self) -> str:
        return f'{self.get_appointment_display()}_{self.person_legal.complete_name}'
