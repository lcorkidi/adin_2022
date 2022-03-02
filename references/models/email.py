from django.db import models

class Email(models.Model):

    email = models.EmailField(
        primary_key=True,
        verbose_name='Correo Electrónico'
    )

    class Meta():
        app_label = 'references'

    def __str__(self) -> str:
        return f'<Email: {self.email}>'