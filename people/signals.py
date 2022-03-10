from django.db.models.signals import pre_save
from django.dispatch import receiver
from scripts.utils import personcompletename

from .models import Person, Person_Natural, Person_Legal

@receiver(pre_save, sender=Person)
def person_save(sender, instance, **kwargs):
    instance.complete_name = personcompletename(instance)

@receiver(pre_save, sender=Person_Legal)
def person_natural_save(sender, instance, **kwargs):
    instance.complete_name = personcompletename(instance)

@receiver(pre_save, sender=Person_Natural)
def person_legal_save(sender, instance, **kwargs):
    instance.complete_name = personcompletename(instance)