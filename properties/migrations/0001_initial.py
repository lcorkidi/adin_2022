# Generated by Django 4.0.2 on 2022-03-04 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('references', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('national_number_1', models.PositiveBigIntegerField(verbose_name='Número Predial Nacional')),
                ('national_number_2', models.PositiveBigIntegerField(verbose_name='Número Predial Nacional')),
                ('national_number_3', models.PositiveBigIntegerField(verbose_name='Número Predial Nacional')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='estates', related_query_name='estate', serialize=False, to='references.address', verbose_name='Dirección')),
                ('total_area', models.FloatField(blank=True, default=None, null=True, verbose_name='Área')),
            ],
            options={
                'verbose_name': 'Predio',
                'verbose_name_plural': 'Predios',
            },
        ),
        migrations.CreateModel(
            name='Realty',
            fields=[
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Apartamento'), (1, 'Local'), (2, 'Oficina'), (3, 'Bodega'), (4, 'Parqueadero'), (5, 'Depósito'), (6, 'Casa'), (7, 'Lote'), (8, 'Finca'), (9, 'Apartaestudio')], verbose_name='Tipo')),
                ('use', models.PositiveSmallIntegerField(choices=[(0, 'Residencial'), (1, 'Comercial'), (2, 'Industrial')], verbose_name='Uso')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='realties', related_query_name='realty', serialize=False, to='references.address', verbose_name='Dirección')),
                ('total_area', models.FloatField(verbose_name='Área')),
            ],
            options={
                'verbose_name': 'Inmueble',
                'verbose_name_plural': 'Inmuebles',
            },
        ),
        migrations.CreateModel(
            name='Realty_Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.DecimalField(decimal_places=4, max_digits=7, verbose_name='Participacion')),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='properties.estate', verbose_name='Predio')),
                ('realty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='properties.realty', verbose_name='Inmueble')),
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
        migrations.CreateModel(
            name='Estate_Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.DecimalField(decimal_places=4, max_digits=7, verbose_name='Participacion')),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='properties.estate', verbose_name='Predio')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.person', verbose_name='Persona')),
            ],
            options={
                'verbose_name': 'Propietario Predio',
                'verbose_name_plural': 'Propietarios Predios',
            },
        ),
        migrations.AddField(
            model_name='estate',
            name='owner',
            field=models.ManyToManyField(related_name='estates', related_query_name='estate', through='properties.Estate_Person', to='people.Person', verbose_name='Propietario(s)'),
        ),
        migrations.CreateModel(
            name='Appraisal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Catastral'), (1, 'Comercial')], verbose_name='Tipo')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('value', models.PositiveBigIntegerField(verbose_name='Valor')),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.estate', verbose_name='Predio')),
            ],
            options={
                'verbose_name': 'Avaluo',
                'verbose_name_plural': 'Avaluos',
            },
        ),
        migrations.AddConstraint(
            model_name='realty_estate',
            constraint=models.UniqueConstraint(fields=('realty', 'estate'), name='unique_realty_estate'),
        ),
        migrations.AddConstraint(
            model_name='estate_person',
            constraint=models.UniqueConstraint(fields=('estate', 'person'), name='unique_estate_person'),
        ),
    ]
