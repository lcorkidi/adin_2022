# Generated by Django 4.0.2 on 2022-03-09 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1, editable=False)),
                ('name', models.CharField(max_length=64, verbose_name='Nombre')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transacción Tipo',
                'verbose_name_plural': 'Transacciones Tipos',
            },
        ),
        migrations.CreateModel(
            name='PUC',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1, editable=False)),
                ('code', models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='Cuenta')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cuenta PUC',
                'verbose_name_plural': 'Cuentas PUC',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1, editable=False)),
                ('code', models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='Código')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Fijo'), (1, 'Movil')], verbose_name='Tipo')),
                ('country', models.PositiveSmallIntegerField(default=57, verbose_name='País')),
                ('region', models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='Región')),
                ('number', models.PositiveIntegerField(verbose_name='Número')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Teléfono',
                'verbose_name_plural': 'Teléfonos',
            },
        ),
        migrations.CreateModel(
            name='E_Mail',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1, editable=False)),
                ('e_mail', models.EmailField(max_length=254, primary_key=True, serialize=False, verbose_name='Correo Electrónico')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Correo Electrónico',
                'verbose_name_plural': 'Correos Electrónicos',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1, editable=False)),
                ('code', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='Código')),
                ('country', models.CharField(max_length=32, verbose_name='País')),
                ('region', models.CharField(max_length=32, verbose_name='Departamento')),
                ('city', models.CharField(max_length=32, verbose_name='Ciudad')),
                ('street_type', models.PositiveSmallIntegerField(choices=[(0, 'Avenida'), (1, 'Calle'), (2, 'Carrera'), (3, 'Diagonal'), (4, 'Transversal'), (5, 'Circunvalar'), (6, 'Circular'), (7, 'Autopista')], verbose_name='Vía')),
                ('street_number', models.PositiveSmallIntegerField(verbose_name='Número Vía')),
                ('street_letter', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E'), (5, 'F'), (6, 'G'), (7, 'H'), (8, 'I'), (9, 'J'), (10, 'K'), (11, 'L'), (12, 'M'), (13, 'M'), (14, 'O'), (15, 'P'), (16, 'Q'), (17, 'R'), (18, 'S'), (19, 'T'), (20, 'U'), (21, 'V'), (22, 'W'), (23, 'X'), (24, 'Y'), (25, 'Z'), (26, 'A1'), (27, 'B1')], default=None, null=True, verbose_name='Letra Vía')),
                ('street_bis', models.BooleanField(blank=True, default=None, null=True, verbose_name='Bis Vía')),
                ('street_bis_complement', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E'), (5, 'F'), (6, 'G'), (7, 'H'), (8, 'I'), (9, 'J'), (10, 'K'), (11, 'L'), (12, 'M'), (13, 'M'), (14, 'O'), (15, 'P'), (16, 'Q'), (17, 'R'), (18, 'S'), (19, 'T'), (20, 'U'), (21, 'V'), (22, 'W'), (23, 'X'), (24, 'Y'), (25, 'Z'), (26, 'A1'), (27, 'B1')], default=None, null=True, verbose_name='Letra Bis Vía')),
                ('street_coordinate', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Norte'), (1, 'Sur'), (2, 'Este'), (3, 'Oeste'), (4, 'Centro')], default=None, null=True, verbose_name='Cardinalidad Vía')),
                ('numeral_number', models.PositiveSmallIntegerField(verbose_name='Número')),
                ('numeral_letter', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E'), (5, 'F'), (6, 'G'), (7, 'H'), (8, 'I'), (9, 'J'), (10, 'K'), (11, 'L'), (12, 'M'), (13, 'M'), (14, 'O'), (15, 'P'), (16, 'Q'), (17, 'R'), (18, 'S'), (19, 'T'), (20, 'U'), (21, 'V'), (22, 'W'), (23, 'X'), (24, 'Y'), (25, 'Z'), (26, 'A1'), (27, 'B1')], default=None, null=True, verbose_name='Letra Número')),
                ('numeral_bis', models.BooleanField(blank=True, default=None, null=True, verbose_name='Bis Número')),
                ('numeral_bis_complement', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E'), (5, 'F'), (6, 'G'), (7, 'H'), (8, 'I'), (9, 'J'), (10, 'K'), (11, 'L'), (12, 'M'), (13, 'M'), (14, 'O'), (15, 'P'), (16, 'Q'), (17, 'R'), (18, 'S'), (19, 'T'), (20, 'U'), (21, 'V'), (22, 'W'), (23, 'X'), (24, 'Y'), (25, 'Z'), (26, 'A1'), (27, 'B1')], default=None, null=True, verbose_name='Letra Bis Número')),
                ('numeral_coordinate', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Norte'), (1, 'Sur'), (2, 'Este'), (3, 'Oeste'), (4, 'Centro')], default=None, null=True, verbose_name='Cardinalidad Número')),
                ('height_number', models.PositiveSmallIntegerField(verbose_name='Altura Nomenclatura')),
                ('interior_group_type', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Bloque'), (1, 'Torre'), (2, 'Edificio')], default=None, null=True, verbose_name='Interior Grupo Tipo')),
                ('interior_group_code', models.CharField(max_length=6, verbose_name='Interior Gruupo Código')),
                ('interior_type', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Apartamento'), (1, 'Local'), (2, 'Oficina'), (3, 'Bodega'), (4, 'Parqueadero'), (5, 'Depósito'), (6, 'Interior'), (7, 'Casa'), (8, 'Lote'), (9, 'Finca'), (10, 'Apartaestudio')], default=None, null=True, verbose_name='Interior Tipo')),
                ('interior_code', models.CharField(max_length=6, verbose_name='Interior Código')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dirección',
                'verbose_name_plural': 'Direcciones',
            },
        ),
        migrations.AddConstraint(
            model_name='phone',
            constraint=models.UniqueConstraint(fields=('country', 'region', 'number'), name='unique_country_region_number'),
        ),
    ]
