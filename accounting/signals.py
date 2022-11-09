from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Ledger
from .utils.models_func import ledger2consecutive, ledger2code

@receiver(pre_save, sender=Ledger)
def ledger_save(sender, instance, **kwargs):
    if not instance.code:
        instance.consecutive = ledger2consecutive(instance)
        instance.code = ledger2code(instance)


