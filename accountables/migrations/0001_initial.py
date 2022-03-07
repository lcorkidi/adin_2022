# Generated by Django 4.0.2 on 2022-03-07 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accountable',
            fields=[
                ('code', models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='Código')),
            ],
            options={
                'verbose_name': 'Contabilizable',
                'verbose_name_plural': 'Contabilizables',
            },
        ),
        migrations.CreateModel(
            name='Lease_Realty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_date', models.DateField(verbose_name='Fecha Contrato')),
                ('start_date', models.DateField(blank=True, default=None, null=True, verbose_name='Fecha Ocupacion')),
                ('end_date', models.DateField(blank=True, default=None, null=True, verbose_name='Fecha Desocupacion')),
            ],
            options={
                'verbose_name': 'Arriendo Inmueble',
                'verbose_name_plural': 'Arriendos Inuembles',
            },
        ),
        migrations.CreateModel(
            name='Lease_Realty_Realty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary', models.BooleanField(verbose_name='Primario')),
                ('lease', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accountables.lease_realty', verbose_name='Contrato')),
                ('realty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='properties.realty', verbose_name='Inmueble')),
            ],
            options={
                'verbose_name': 'Inmueble Arriendo Inmueble',
                'verbose_name_plural': 'Inmuebles Arriendos Inmuebles',
            },
        ),
        migrations.CreateModel(
            name='Lease_Realty_Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.PositiveSmallIntegerField(choices=[(0, 'Arrendador'), (1, 'Arrendatario'), (2, 'Fiador')], verbose_name='Rol')),
                ('lease', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accountables.lease_realty', verbose_name='Contrato')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.person', verbose_name='Persona')),
            ],
            options={
                'verbose_name': 'Parte Arriendo Inmueble',
                'verbose_name_plural': 'Partes Arriendos Inmuebles',
            },
        ),
        migrations.AddField(
            model_name='lease_realty',
            name='part',
            field=models.ManyToManyField(related_name='lease_realty', related_query_name='leases_realties', through='accountables.Lease_Realty_Person', to='people.Person', verbose_name='Parte'),
        ),
        migrations.AddField(
            model_name='lease_realty',
            name='realty',
            field=models.ManyToManyField(related_name='lease_realty', related_query_name='leases_realties', through='accountables.Lease_Realty_Realty', to='properties.Realty', verbose_name='Inmueble'),
        ),
        migrations.CreateModel(
            name='Date_Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('value', models.PositiveIntegerField(verbose_name='Valor')),
                ('accountable', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='date_value', related_query_name='dates_values', to='accountables.accountable', verbose_name='Contabilizable')),
            ],
            options={
                'verbose_name': 'Fecha Valor',
                'verbose_name_plural': 'Fechas Valores',
            },
        ),
        migrations.AddConstraint(
            model_name='date_value',
            constraint=models.UniqueConstraint(fields=('accountable', 'date'), name='unique_accountable_date'),
        ),
    ]
