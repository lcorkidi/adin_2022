from django.db import models
from django.conf import settings

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(state=0)

class BaseModel(models.Model):

    STATE_CHOICE = [(0,'Inactivo'),
                    (1,'Por Revisar'),
                    (2,'Revisado')]
                    
    state_change_user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                editable=False,
                                on_delete=models.PROTECT)
    state_change_date = models.DateTimeField(auto_now=True)
    state = models.PositiveSmallIntegerField(choices=STATE_CHOICE, 
                                 default=1,
                                 editable=False)

    class Meta:
        abstract = True
