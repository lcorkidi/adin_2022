from django.db import models
from django.contrib.contenttypes.models import ContentType

class Error(models.Model):

    TYPE_CHOICE = [
        (0,'Validacion Objeto'),
        (1,'Procesos Pendientes Objeto'),
        (2, 'Integridad Datos Objeto')
    ]

    code = models.CharField(
        primary_key=True,
        max_length=128,
        verbose_name='Código'
    )
    model = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
        verbose_name='Modelo'
    )
    type = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICE,
        verbose_name='Tipo'
    )
    is_m2m = models.BooleanField(
        verbose_name='Es Relacion Multiple'
    )
    field_name = models.CharField(
        max_length=64,
        verbose_name='Nombre Campo'
    )
    description = models.TextField(
        max_length=512,
        verbose_name='Descripcion'
    )
    
    class Meta:
        app_label = 'errors'
        verbose_name = 'Error'
        verbose_name_plural = 'Errores'

    def __repr__(self):
        return f'<Error: {self.code}>'

    def __str__(self):
        return f'{self.get_type_display().upper()}-{self.model.name.upper()}-{self.field_name.upper()}-{self.code[-4:]}'
