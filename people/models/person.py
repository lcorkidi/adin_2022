from django.db import models

class Person(models.Model):
    ID_TYPE_CHOICE = [
        (0, 'CC'),
        (1, 'NIT'),
        (2, 'TI'),
        (3, 'CE')
    ]
    PERSON_TYPE_CHOICE = [
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
    person_type = models.PositiveSmallIntegerField(
        choices=PERSON_TYPE_CHOICE,
        verbose_name='Tipo Persona'
    )
    name = models.CharField(
        max_length=64,
        verbose_name='Nombre(s)'
    )

    class Meta:
        app_label = 'people'

    def __str__(self) -> str:
        if self.person_type == 0:
            return Person_Natural(self)
        elif self.person_type == 1:
            return Person_Legal(self)

class Person_Natural(Person):
    last_name = models.CharField(
        max_length=64,
        verbose_name='Apellido(s)'
    )

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'

class Person_Legal(Person):
    PERSON_LEGAL_TYPE_CHOICE = [
        (0, 'S.A.'),
        (1, 'S.A.S'),
        (2, 'LTDA.'),
        (3, 'E.U.'),
        (4, '& CIA.'),
        (5, 'S. en C.') 
    ]
    person_legal_type = models.PositiveSmallIntegerField(
        choices=PERSON_LEGAL_TYPE_CHOICE,
        verbose_name='Tipo de Sociedad'
    )
    
    def __str__(self) -> str:
        return f'{self.name} {self.get_person_legal_type_display()}'

