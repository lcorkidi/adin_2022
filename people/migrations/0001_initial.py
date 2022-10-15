# Generated by Django 4.0.5 on 2022-10-15 00:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('references', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('id_number', models.PositiveSmallIntegerField(primary_key=True, serialize=False, verbose_name='Número DI')),
                ('id_type', models.PositiveSmallIntegerField(choices=[(0, 'CC'), (1, 'NIT'), (2, 'TI'), (3, 'CE')], verbose_name='Tipo DI')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Natural'), (1, 'Jurídica')], verbose_name='Tipo Persona')),
                ('name', models.CharField(max_length=64, verbose_name='Nombre(s)')),
                ('complete_name', models.CharField(max_length=128, verbose_name='Nombre Completo')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'ordering': ['complete_name'],
                'permissions': [('activate_person', 'Can activate person.')],
            },
        ),
        migrations.CreateModel(
            name='Person_Legal',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='people.person')),
                ('legal_type', models.PositiveSmallIntegerField(choices=[(0, 'S.A.'), (1, 'S.A.S.'), (2, 'LTDA.'), (3, 'E.U.'), (4, '& CIA.'), (5, 'S. en C.')], verbose_name='Tipo de Sociedad')),
            ],
            options={
                'verbose_name': 'Persona Jurídica',
                'verbose_name_plural': 'Personas Jurídicas',
                'ordering': ['complete_name'],
            },
            bases=('people.person',),
        ),
        migrations.CreateModel(
            name='Person_Natural',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='people.person')),
                ('last_name', models.CharField(max_length=64, verbose_name='Apellido(s)')),
            ],
            options={
                'verbose_name': 'Persona Natural',
                'verbose_name_plural': 'Personas Naturales',
                'ordering': ['complete_name'],
            },
            bases=('people.person',),
        ),
        migrations.CreateModel(
            name='Person_Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('use', models.PositiveSmallIntegerField(choices=[(0, 'Personal'), (1, 'Residencia'), (2, 'Auxiliar Administrativo'), (3, 'Auxiliar Contable')], verbose_name='Uso')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.person', verbose_name='Persona')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='references.phone', verbose_name='Teléfono')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Teléfono Persona',
                'verbose_name_plural': 'Teléfonos Personas',
            },
        ),
        migrations.CreateModel(
            name='Person_E_Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('use', models.PositiveSmallIntegerField(choices=[(0, 'Principal'), (1, 'Adicional')], verbose_name='Uso')),
                ('e_mail', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='references.e_mail', verbose_name='Correo Electrónico')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.person', verbose_name='Persona')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Correo Electrónico Personas',
                'verbose_name_plural': 'Correos Electrónicos Personas',
            },
        ),
        migrations.CreateModel(
            name='Person_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('use', models.PositiveSmallIntegerField(choices=[(0, 'Residencia'), (1, 'Trabajo'), (2, 'Planta'), (3, 'Administración'), (4, 'Punto de Venta'), (5, 'Establecimiento de Comercio')], verbose_name='Uso')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='references.address', verbose_name='Dirección')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.person', verbose_name='Persona')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dirección Persona',
                'verbose_name_plural': 'Direcciones Personas',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.ManyToManyField(blank=True, related_name='people', related_query_name='person', through='people.Person_Address', to='references.address', verbose_name='Dirección'),
        ),
        migrations.AddField(
            model_name='person',
            name='e_mail',
            field=models.ManyToManyField(blank=True, related_name='people', related_query_name='person', through='people.Person_E_Mail', to='references.e_mail', verbose_name='Correo Electrónico'),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.ManyToManyField(blank=True, related_name='people', related_query_name='person', through='people.Person_Phone', to='references.phone', verbose_name='Teléfono'),
        ),
        migrations.AddField(
            model_name='person',
            name='state_change_user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Person_Legal_Person_Natural',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('appointment', models.PositiveSmallIntegerField(choices=[(0, 'Representate Legal'), (1, 'Gerente General'), (2, 'Suplente'), (3, 'Auxiliar Administración'), (4, 'Auxialr Contabilidad'), (5, 'Supervisor Planta'), (6, 'Socio')], verbose_name='Cargo')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('person_legal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.person_legal', verbose_name='Empresa')),
                ('person_natural', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.person_natural', verbose_name='Personal')),
            ],
            options={
                'verbose_name': 'Personal',
                'verbose_name_plural': 'Personal',
            },
        ),
        migrations.AddField(
            model_name='person_legal',
            name='staff',
            field=models.ManyToManyField(blank=True, related_name='people_legal', related_query_name='person_legal', through='people.Person_Legal_Person_Natural', to='people.person_natural', verbose_name='Personal'),
        ),
    ]
