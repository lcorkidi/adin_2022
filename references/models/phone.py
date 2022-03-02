from django.db import models

class Phone(models.Model):

    TYPE_CHOICE = [
        (0, 'Fijo'),
        (1, 'Movil')
    ]

    type = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICE,
        verbose_name='Tipo'
    )
    country = models.CharField(
        max_length=32,
        default='Colombia',
        verbose_name='País'
    )
    city = models.CharField(
        max_length=32,
        default='Cali',
        verbose_name='Ciudad'
    )
    number = models.PositiveSmallIntegerField(
        verbose_name='Número'
    )

    class Meta():
        app_label = 'references'

    def __str__(self) -> str:
        return f'<Phone: {self.number}' if self.type == 0 else f'<Phone: {self.city}-{self.number}'