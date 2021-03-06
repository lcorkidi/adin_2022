from django.db import models
from adin.core.models import BaseModel

class Transaction_Type(BaseModel):

    name =  models.CharField(
        max_length=64,
        primary_key=True,
        verbose_name='Nombre'
    )

    class Meta:
        app_label = 'references'
        verbose_name = 'Transacción Tipo'
        verbose_name_plural = 'Transacciones Tipos'
        permissions = [
            ('activate_transaction_type', 'Can activate transaction type.'),
        ]

    def __repr__(self) -> str:
        return f'<Transaction: {self.name}>'
    
    def __str__(self) -> str:
        return self.name