from django.db import models

from .accountable import Accountable

class Utility_Contract(Accountable):

    utility = models.ManyToManyField(
        'references.Utility', 
        related_name='utility_contract',
        related_query_name='utility_contracts',
        verbose_name='Servicio Publico'
    )
    realty = models.ForeignKey(
        'properties.Realty', 
        on_delete=models.PROTECT,
        related_name='utility_contract',
        related_query_name='utility_contracts',
        verbose_name='Inmueble'
    )
    holder = models.ForeignKey(
        'properties.Person', 
        on_delete=models.PROTECT,
        related_name='holder_utility_contract',
        related_query_name='holder_utility_contracts',
        verbose_name='Titular'
    )
    provider = models.ForeignKey(
        'properties.Person', 
        on_delete=models.PROTECT,
        related_name='provider_utility_contract',
        related_query_name='provider_utility_contracts',
        verbose_name='Proveedor'
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
