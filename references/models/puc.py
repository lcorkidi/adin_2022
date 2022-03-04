from django.db import models

class PUC(models.Model):

    code = models.PositiveBigIntegerField( 
        primary_key=True,
        verbose_name='Cuenta'
        )
    name = models.CharField(
        max_length=100,
        verbose_name='Nombre'
        )

    class Meta:
        app_label = 'references'
        verbose_name = 'Cuenta PUC'
        verbose_name_plural = 'Cuentas PUC'

    def __repr__(self) -> str:
        return f'<Puc: {self.code}>'

    def __str__(self):
        return self.code
