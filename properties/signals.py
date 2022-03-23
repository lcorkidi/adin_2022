from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Realty

@receiver(pre_save, sender=Realty)
def realty_save(sender, instance, **kwargs):
    if not instance.code:
        instance.code = instance.address.code

