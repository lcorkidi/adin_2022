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

    class Meta:
        app_label = 'accountables'
        verbose_name = 'Contabilizable'
        verbose_name_plural = 'Contabilizables'

    def subclass_obj(self):
        return self.subclass.model_class().active.get(code=self.code)

    def ledger_holder(self):
        return self.subclass_obj().ledger_holder()

    def ledger_third_party(self):
        return self.subclass_obj().ledger_third_party()

    def __str__(self) -> str:
        return self.code
