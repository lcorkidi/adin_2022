# Generated by Django 4.0.2 on 2022-07-13 20:34

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
            name='Charge_Factor',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('name', models.CharField(max_length=63, primary_key=True, serialize=False)),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tasa Transacción',
                'verbose_name_plural': 'Tasas Transacciones',
                'permissions': [('activate_charge_factor', 'Can activate charge factor.')],
            },
        ),
        migrations.CreateModel(
            name='PUC',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
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
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
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
                'ordering': ['code'],
                'permissions': [('activate_phone', 'Can activate phone.')],
            },
        ),
        migrations.CreateModel(
            name='Factor_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('validity_date', models.DateField(verbose_name='Fecha Validez')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Monto')),
                ('percentage', models.DecimalField(decimal_places=3, default=100, max_digits=6, verbose_name='Porcentaje')),
                ('in_instance_attribute', models.CharField(blank=True, default=None, max_length=15, null=True, verbose_name='Atributo en Instancia')),
                ('factor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='datas', related_query_name='data', to='references.charge_factor', verbose_name='Tasa')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Datos Tasas',
                'verbose_name_plural': 'Datos Tasas',
            },
        ),
        migrations.CreateModel(
            name='E_Mail',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('e_mail', models.EmailField(max_length=254, primary_key=True, serialize=False, verbose_name='Correo Electrónico')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Correo Electrónico',
                'verbose_name_plural': 'Correos Electrónicos',
                'ordering': ['e_mail'],
                'permissions': [('e_mail', 'Can activate e-mail.')],
            },
        ),
        migrations.CreateModel(
            name='Calendar_Date',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('name', models.CharField(max_length=63, primary_key=True, serialize=False, verbose_name='Descripción')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Fecha Calendario',
                'verbose_name_plural': 'Fechas Calendario',
                'ordering': ['name'],
                'permissions': [('calendar_date', 'Can activate calendar_date.')],
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
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
                ('interior_group_code', models.CharField(blank=True, default=None, max_length=6, null=True, verbose_name='Interior Grupo Código')),
                ('interior_type', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Apartamento'), (1, 'Local'), (2, 'Oficina'), (3, 'Bodega'), (4, 'Parqueadero'), (5, 'Depósito'), (6, 'Interior'), (7, 'Casa'), (8, 'Lote'), (9, 'Finca'), (10, 'Apartaestudio')], default=None, null=True, verbose_name='Interior Tipo')),
                ('interior_code', models.CharField(blank=True, default=None, max_length=6, null=True, verbose_name='Interior Código')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dirección',
                'verbose_name_plural': 'Direcciones',
                'ordering': ['code'],
                'permissions': [('address', 'Can activate address.')],
            },
        ),
        migrations.AddConstraint(
            model_name='phone',
            constraint=models.UniqueConstraint(fields=('country', 'region', 'number'), name='unique_country_region_number'),
        ),
        migrations.AddConstraint(
            model_name='factor_data',
            constraint=models.UniqueConstraint(fields=('factor', 'validity_date'), name='unique_factor_validity'),
        ),
        migrations.AddConstraint(
            model_name='factor_data',
            constraint=models.CheckConstraint(check=models.Q(('percentage__gte', 0), ('percentage__lte', 100)), name='facdat_percentage_gte_0_and_lte_100'),
        ),
    ]
