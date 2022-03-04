from django.db import models
from accounting.core import Account_Structure

class Account(models.Model):
    
    code = models.CharField(
        primary_key=True,
        max_length=10,
    )

    description = models.TextField(
        max_length=255,
        blank=True,
    )

    class Meta:
        app_label = 'accounting'
        ordering = ['code'] 

    @property
    def levels(self):
        return Account_Structure.levels(self.code)

    @property
    def nature(self):
        return Account_Structure.nature(self.code)

    def __repr__(self) -> str:
        return f'<Acc: {self.code}>'
    
    def __str__(self) -> str:
        return f'Acc. {self.code}'