from django.db import models

from adin.core.models import BaseModel

class Utility(BaseModel):

    name =  models.CharField(
        max_length=64,
        primary_key=True,
        verbose_name='Nombre'
    )

    class Meta:
        app_label = 'references'
        verbose_name = 'Servicio Publico'
        verbose_name_plural = 'Servicios Publicos'
        permissions = [
            ('activate_utility', 'Can activate utility.'),
            ('check_utility', 'Can check utlity.'),
        ]

    def __repr__(self) -> str:
        return f'<Utility: {self.name}>'
    
    def __str__(self) -> str:
        return self.name
