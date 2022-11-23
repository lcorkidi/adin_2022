from django.db import models

from .accountable import Accountable

class Utiliy_Contract(Accountable):

    realty = models.ManyToManyField(
        'properties.Realty', 
        through='Utiliy_Contract_Realty', 
        through_fields=('utility_contract', 'realty'),
        related_name='utility_contract',
        related_query_name='utility_contracts',
        verbose_name='Inmueble'
    )
    part = models.ManyToManyField(
        'people.Person', 
        through='Utiliy_Contract_Person', 
        through_fields=('utility_contract', 'person'),
        related_name='utility_contract',
        related_query_name='utility_contracts',
        verbose_name='Parte'
    )

    
    class Meta:
        app_label = 'accountables'
        verbose_name = 'Contrato Servicio Publico'
        verbose_name_plural = 'Contratos Servicio Publico'
        permissions = [
            ('activate_utility_contract', 'Can activate utility contract.'),
            ('check_utility_contract', 'Can check utility contract.'),
            ('accounting_utility_contract', 'Can do accounting on utility contract.'),
        ]
