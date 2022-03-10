from django.db.models.signals import pre_save
from django.dispatch import receiver
from scripts.utils import address2code, phone2code

from .models import Address, Phone

@receiver(pre_save, sender=Address)
def address_save(sender, instance, **kwargs):
    instance.code = address2code(instance)

@receiver(pre_save, sender=Phone)
def phone_save(sender, instance, **kwargs):
    instance.code = phone2code(instance)

