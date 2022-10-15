from django.db import models
from django.contrib.contenttypes.models import ContentType

from adin.core.models import BaseModel

class Ledger(BaseModel):

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
        related_name='ledgers_holders',
        related_query_name='ledger_holder',
        verbose_name='Titular'
    )    
    third_party = models.ForeignKey(
        'people.Person',
        on_delete=models.PROTECT,
        related_name='ledgers_third_parties',
        related_query_name='ledger_third_party',
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
        permissions = [
            ('activate_ledger', 'Can activate ledger.'),
        ]

    def __repr__(self) -> str:
        return f'<Ledger: {self.code}^{self.date.strftime("%Y-%m-%d")}_{self.third_party}>'

    def __str__(self) -> str:
        return f'{self.code}^{self.date.strftime("%Y-%m-%d")}_{self.third_party}'

class Ledger_Type(BaseModel):
    
    name =  models.CharField(
        max_length=64,
        primary_key=True,
        verbose_name='Nombre'
    )
    abreviation =  models.CharField(
        max_length=4,
        verbose_name='Abreviación'
    )    

    class Meta:
        app_label = 'accounting'
        verbose_name = 'Registro Tipo'
        verbose_name_plural = 'Registros Tipos'
        permissions = [
            ('activate_ledger_type', 'Can activate ledger type.'),
            ('check_ledger_type', 'Can check ledger type.'),
        ]

    def __repr__(self) -> str:
        return f'<Ledger_Type: {self.name}>'
    
    def __str__(self) -> str:
        return self.name

class Ledger_Template(BaseModel):

    code = models.CharField(
        max_length=128,
        primary_key=True
    )
    accountable_class = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
        verbose_name='Clase Contabilizable'
    )
    transaction_type = models.ForeignKey(
        'accountables.Accountable_Transaction_Type',
        on_delete=models.PROTECT,
        related_name='ledgers_templates',
        related_query_name='ledger_template',
        verbose_name='Tipo Transacción'
    )
    ledger_type = models.ForeignKey(
        Ledger_Type,
        on_delete=models.PROTECT,
        related_name='ledgers_templates',
        related_query_name='ledger_template',
        verbose_name='Tipo Registro'
    )
    concept_dependant = models.BooleanField(
        verbose_name='Requiere Concepto'
    )
    
    class Meta:
        app_label = 'accounting'
        verbose_name = 'Formato Registro'
        verbose_name_plural = 'Formatos Registros'
        constraints = [
            models.UniqueConstraint(fields=['transaction_type', 'ledger_type'], name='unique_trancaction_ledger_types'),
        ]
        
    def ledger_from_template(self, charge_concept, date, user):
        ledger = Ledger(
            state_change_user=user,
            type=self.ledger_type,
            holder=charge_concept.accountable.ledger_holder(),
            third_party=charge_concept.accountable.ledger_third_party(),
            date=date
        )
        ledger.save()

        for charge_template in self.charges_templates.all():
            charge_template.charge_from_template(ledger, charge_concept, user)

    def __repr__(self) -> str:
        return f'<Ledger_Template: {self.code}>'
    
    def __str__(self) -> str:
        return self.code
