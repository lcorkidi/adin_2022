# Generated by Django 4.0.2 on 2022-05-02 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('references', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('national_number', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Número Predial Nacional')),
                ('total_area', models.FloatField(blank=True, default=None, null=True, verbose_name='Área')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='estates', related_query_name='estate', to='references.address', verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Predio',
                'verbose_name_plural': 'Predios',
                'permissions': [('activate_estate', 'Can activate estate.')],
            },
        ),
        migrations.CreateModel(
            name='Realty',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Apartamento'), (1, 'Local'), (2, 'Oficina'), (3, 'Bodega'), (4, 'Parqueadero'), (5, 'Depósito'), (6, 'Casa'), (7, 'Lote'), (8, 'Finca'), (9, 'Apartaestudio')], verbose_name='Tipo')),
                ('use', models.PositiveSmallIntegerField(choices=[(0, 'Residencial'), (1, 'Comercial'), (2, 'Industrial')], verbose_name='Uso')),
                ('code', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='Código')),
                ('total_area', models.FloatField(verbose_name='Área')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='realties', related_query_name='realty', to='references.address', verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Inmueble',
                'verbose_name_plural': 'Inmuebles',
                'ordering': ['code'],
                'permissions': [('activate_realty', 'Can activate realty.')],
            },
        ),
        migrations.CreateModel(
            name='Realty_Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('percentage', models.DecimalField(decimal_places=4, max_digits=7, verbose_name='Participacion')),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='properties.estate', verbose_name='Predio')),
                ('realty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='properties.realty', verbose_name='Inmueble')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Predio Inmueble',
                'verbose_name_plural': 'Predios Inmuebles',
            },
        ),
        migrations.AddField(
            model_name='realty',
            name='estate',
            field=models.ManyToManyField(related_name='realties', related_query_name='realty', through='properties.Realty_Estate', to='properties.Estate', verbose_name='Predio(s)'),
        ),
        migrations.AddField(
            model_name='realty',
            name='state_change_user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Estate_Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('percentage', models.DecimalField(decimal_places=4, max_digits=7, verbose_name='Participacion')),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='properties.estate', verbose_name='Predio')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.person', verbose_name='Persona')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Propietario Predio',
                'verbose_name_plural': 'Propietarios Predios',
            },
        ),
        migrations.CreateModel(
            name='Estate_Appraisal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Catastral'), (1, 'Comercial')], verbose_name='Tipo')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('value', models.PositiveBigIntegerField(verbose_name='Valor')),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estates_appraisals', related_query_name='estate_appraisal', to='properties.estate', verbose_name='Predio')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Avaluo Predio',
                'verbose_name_plural': 'Avaluos Predios',
            },
        ),
        migrations.AddField(
            model_name='estate',
            name='owner',
            field=models.ManyToManyField(related_name='estates', related_query_name='estate', through='properties.Estate_Person', to='people.Person', verbose_name='Propietario(s)'),
        ),
        migrations.AddField(
            model_name='estate',
            name='state_change_user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='realty_estate',
            constraint=models.UniqueConstraint(fields=('realty', 'estate'), name='unique_realty_estate'),
        ),
        migrations.AddConstraint(
            model_name='realty',
            constraint=models.UniqueConstraint(fields=('code', 'address'), name='realty_unique_code_address'),
        ),
        migrations.AddConstraint(
            model_name='estate_person',
            constraint=models.UniqueConstraint(fields=('estate', 'person'), name='unique_estate_person'),
        ),
        migrations.AddConstraint(
            model_name='estate',
            constraint=models.UniqueConstraint(fields=('national_number', 'address'), name='unique_code_address'),
        ),
    ]
