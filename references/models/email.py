from django.db import models

class Email(models.Model):

    email = models.EmailField(
        primary_key=True,
        verbose_name='Correo Electrónico'
    )

    class Meta:
        app_label = 'references'
        verbose_name = 'Correo Electrónico'
        verbose_name_plural = 'Correos Electrónicos'

    def __str__(self) -> str:
        return f'<Email: {self.email}>'