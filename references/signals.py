from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Address, Phone
from .utils import address2code, phone2code

@receiver(pre_save, sender=Address)
def address_save(sender, instance, **kwargs):
    if not instance.code:
        instance.code = address2code(instance)

@receiver(pre_save, sender=Phone)
def phone_save(sender, instance, **kwargs):
    if not instance.code:
        instance.code = phone2code(instance)

