from django.db import models
from adin.core.models import BaseModel

class E_Mail(BaseModel):

    e_mail = models.EmailField(
        primary_key=True,
        verbose_name='Correo Electrónico'
    )

    class Meta:
        app_label = 'references'
        verbose_name = 'Correo Electrónico'
        verbose_name_plural = 'Correos Electrónicos'
        ordering = ['e_mail']
        permissions = [
            ('e_mail', 'Can activate e-mail.'),
        ]

    def __repr__(self) -> str:
        return f'<Email: {self.e_mail}>'

    def __str__(self) -> str:
        return self.e_mail