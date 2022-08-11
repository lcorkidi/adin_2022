from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Accountable_Concept
from .utils import accon_2_code

@receiver(pre_save, sender=Accountable_Concept)
def accountable_concept_save(sender, instance, **kwargs):
    if not instance.code:
        instance.code = accon_2_code(instance)

