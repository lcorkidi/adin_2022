from django.db import models
from django.conf import settings

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(state=0)

class InactiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=0)

class BaseModel(models.Model):

    STATE_CHOICE = [
        (0, 'Inactivo'),
        (1, 'Por Correguir'),
        (2, 'Por Revisar'),
        (3, 'Revisado')
    ]
                    
    state_change_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        editable=False
    )
    state_change_date = models.DateTimeField(
        auto_now=True
    )
    state = models.PositiveSmallIntegerField(
        choices=STATE_CHOICE, 
        default=1
    )

    objects = models.Manager()
    active = ActiveManager()
    inactive = InactiveManager()

    class Meta:
        abstract = True
