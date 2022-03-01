from django.db import models

class Address(models.Model):

    def __str__(self) -> str:
        return 'Address'