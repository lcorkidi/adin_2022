from django.db import models
from django.contrib.contenttypes.models import ContentType

from adin.core.models import BaseModel

class Accountable(BaseModel):

    code = models.CharField(
        primary_key=True,
        max_length=64,
        verbose_name='Código'
    )
    subclass = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
        verbose_name='Subclase'
    )
    transaction_types = models.ManyToManyField(
        'references.Transaction_Type',
        related_name='accountables',
        related_query_name='accountable',
        verbose_name='Tipos de Cargo'
    )

    class Meta:
        app_label = 'accountables'
        verbose_name = 'Contabilizable'
        permissions = [
            ('accounting_accountable', 'Can do accountable accounting.')
        ]

    def subclass_obj(self):
        return self.subclass.model_class().active.get(code=self.code)

    def __repr__(self) -> str:
        return f'<Accountable: {self.code}>'

    def __str__(self) -> str:
        return self.code
