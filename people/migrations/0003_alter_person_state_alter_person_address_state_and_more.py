# Generated by Django 4.0.2 on 2022-03-23 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_alter_person_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1),
        ),
        migrations.AlterField(
            model_name='person_address',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1),
        ),
        migrations.AlterField(
            model_name='person_e_mail',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1),
        ),
        migrations.AlterField(
            model_name='person_legal_person_natural',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1),
        ),
        migrations.AlterField(
            model_name='person_phone',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1),
        ),
    ]
