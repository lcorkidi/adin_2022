from django.db import models

class Lease_Realty(models.Model):

    realty = models.ManyToManyField(
        'properties.Realty', 
        through='Lease_Realty_Realty', 
        through_fields=('lease', 'realty'),
        related_name='lease_realty',
        related_query_name='leases_realties',
        verbose_name='Inmueble'
    )
    part = models.ManyToManyField(
        'people.Person', 
        through='Lease_Realty_Person', 
        through_fields=('lease', 'person'),
        related_name='lease_realty',
        related_query_name='leases_realties',
        verbose_name='Parte'
    )
    doc_date = models.DateField(
        verbose_name='Fecha Contrato'
    )
    start_date = models.DateField(
        null=True,
        blank=True,
        default=None,
        verbose_name='Fecha Ocupacion'
    )
    end_date = models.DateField(
        null=True,
        blank=True,
        default=None,
        verbose_name='Fecha Desocupacion'
    )
    
    class Meta:
        app_label = 'accountables'
        verbose_name = 'Arriendo Inmueble'
        verbose_name_plural = 'Arriendos Inuembles'

    def __repr__(self) -> str:
        return f'<Lease_Realty: {self.name}>'
    
    def __str__(self) -> str:
        return self.name

class Lease_Realty_Realty(models.Model):

    lease = models.ForeignKey(
        Lease_Realty,
        on_delete=models.PROTECT,
        verbose_name='Contrato'
    )
    realty = models.ForeignKey(
        'properties.Realty',
        on_delete=models.PROTECT,
        verbose_name='Inmueble'
    )
    primary = models.BooleanField(
        verbose_name='Primario'
    )
 
    class Meta:
        app_label = 'accountables'
        verbose_name = 'Inmueble Arriendo Inmueble'
        verbose_name_plural = 'Inmuebles Arriendos Inmuebles'

    def __repr__(self) -> str:
        return f'<Lease_Realty_Person: {self.lease.pk}_{self.realty.pk}>'
    
    def __str__(self) -> str:
        return f'{self.lease.pk}_{self.realty.pk}'

class Lease_Realty_Person(models.Model):

    ROLE_CHOICE = [
        (0,'Arrendador'),
        (1,'Arrendatario'),
        (2,'Fiador')
    ]
    
    lease = models.ForeignKey(
        Lease_Realty,
        on_delete=models.PROTECT,
        verbose_name='Contrato'
    )
    person = models.ForeignKey(
        'people.Person',
        on_delete=models.PROTECT,
        verbose_name='Persona'
    )
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICE,
        verbose_name='Rol'
    )
    phone = models.ForeignKey(
        'references.Phone',
        on_delete=models.PROTECT,
        verbose_name='Teléfono'
    )
    email = models.ForeignKey(
        'references.Email',
        on_delete=models.PROTECT,
        verbose_name='Correo Electrónico',
    )
    address = models.ForeignKey(
        'references.Address',
        on_delete=models.PROTECT,
        verbose_name='Dirección'
    )
 
    class Meta:
        app_label = 'accountables'
        verbose_name = 'Parte Arriendo Inmueble'
        verbose_name_plural = 'Partes Arriendos Inmuebles'

    def __repr__(self) -> str:
        return f'<Lease_Realty_Person: {self.lease.pk}_{self.person.complete_name}>'
    
    def __str__(self) -> str:
        return f'{self.lease.pk}_{self.person.complete_name}'
