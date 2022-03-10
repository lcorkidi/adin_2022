from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Estate, Realty

@receiver(pre_save, sender=Estate)
def address_save(sender, instance, **kwargs):
    if not instance.code:
        instance.code = instance.address.code

@receiver(pre_save, sender=Realty)
def phone_save(sender, instance, **kwargs):
    if not instance.code:
        instance.code = instance.address.code

