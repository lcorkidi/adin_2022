# Generated by Django 4.0.2 on 2022-03-23 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_alter_person_state_alter_person_address_state_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'permissions': [('activate_person', 'Can activate person.')], 'verbose_name': 'Persona', 'verbose_name_plural': 'Personas'},
        ),
        migrations.AlterModelOptions(
            name='person_address',
            options={'permissions': [('activate_person_address', 'Can activate person`s address.')], 'verbose_name': 'Dirección Persona', 'verbose_name_plural': 'Direcciones Personas'},
        ),
        migrations.AlterModelOptions(
            name='person_e_mail',
            options={'permissions': [('activate_person_e_mail', 'Can activate person`s e-mail.')], 'verbose_name': 'Correo Electrónico Personas', 'verbose_name_plural': 'Correos Electrónicos Personas'},
        ),
        migrations.AlterModelOptions(
            name='person_legal_person_natural',
            options={'permissions': [('activate_person_legal_person_natural', 'Can activate company`s staff.')], 'verbose_name': 'Personal', 'verbose_name_plural': 'Personal'},
        ),
        migrations.AlterModelOptions(
            name='person_phone',
            options={'permissions': [('activate_person_phone', 'Can activate person`s phone.')], 'verbose_name': 'Teléfono Persona', 'verbose_name_plural': 'Teléfonos Personas'},
        ),
    ]
