from django.db import models
from adin.core.models import BaseModel

class Transaction_Type(BaseModel):

    name =  models.CharField(
        max_length=64,
        verbose_name='Nombre'
    )

    class Meta:
        app_label = 'references'
        verbose_name = 'Transacción Tipo'
        verbose_name_plural = 'Transacciones Tipos'

    def __repr__(self) -> str:
        return f'<Transaction: {self.name}>'
    
    def __str__(self) -> str:
        return self.name