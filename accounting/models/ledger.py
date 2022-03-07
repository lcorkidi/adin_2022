from django.db import models

class Ledger(models.Model):

    code = models.CharField(
        primary_key=True,
        max_length=64,
        verbose_name='Código'
    )
    type = models.ForeignKey(
        'accounting.Ledger_Type',
        on_delete=models.PROTECT,
        related_name='ledgers',
        related_query_name='ledger',
        verbose_name='Tipo'
    )
    consecutive = models.PositiveIntegerField(
        verbose_name='Consecutivo'
    )
    description = models.TextField(
        max_length=255,
        verbose_name='Descripción',
        blank=True,
        null=True,
        default=None
    )
    holder = models.ForeignKey(
        'people.Person',
        on_delete=models.PROTECT,
        related_name='ledgers',
        related_query_name='ledger',
        verbose_name='Titular'
    )    
    third_party = models.ForeignKey(
        'people.Person',
        on_delete=models.PROTECT,
        related_name='ledgers',
        related_query_name='ledger',
        verbose_name='Tercero'
    )
    date = models.DateField(
        verbose_name='Fecha'
    )

    class Meta:
        app_label = 'accounting'
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
        constraints = [
            models.UniqueConstraint(fields=['type', 'consecutive'], name='unique_type_consecutive'),
        ]

    def __repr__(self) -> str:
        return f'<Ledger: {self.code}_{self.third_party.pk}>'

    def __str__(self) -> str:
        return f'{self.code}_{self.third_party.pk}'

class Ledger_Type(models.Model):
    
    name =  models.CharField(
        max_length=64,
        verbose_name='Nombre'
    )

    class Meta:
        app_label = 'accounting'
        verbose_name = 'Registro Tipo'
        verbose_name_plural = 'Registros Tipos'

    def __repr__(self) -> str:
        return f'<Ledger_Type: {self.name}>'
    
    def __str__(self) -> str:
        return self.name