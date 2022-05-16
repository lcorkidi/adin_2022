from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Ledger, Ledger_Template
from .utils import ledger2consecutive, ledger2code, ledgertemplate2code

@receiver(pre_save, sender=Ledger)
def ledger_save(sender, instance, **kwargs):
    if not instance.code:
        instance.consecutive = ledger2consecutive(instance)
        instance.code = ledger2code(instance)

@receiver(pre_save, sender=Ledger_Template)
def ledger_template_save(sender, instance, **kwargs):
    if not instance.code:
        instance.code = ledgertemplate2code(instance)


