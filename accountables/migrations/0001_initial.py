# Generated by Django 4.0.2 on 2022-06-28 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('references', '0001_initial'),
        ('people', '0001_initial'),
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accountable',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('code', models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='Código')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('subclass', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.contenttype', verbose_name='Subclase')),
            ],
            options={
                'verbose_name': 'Contabilizable',
                'permissions': [('accounting_accountable', 'Can do accountable accounting.')],
            },
        ),
        migrations.CreateModel(
            name='Lease_Realty',
            fields=[
                ('accountable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accountables.accountable')),
                ('doc_date', models.DateField(verbose_name='Fecha Contrato')),
                ('start_date', models.DateField(blank=True, default=None, null=True, verbose_name='Fecha Ocupacion')),
                ('end_date', models.DateField(blank=True, default=None, null=True, verbose_name='Fecha Desocupacion')),
            ],
            options={
                'verbose_name': 'Arriendo Inmueble',
                'verbose_name_plural': 'Arriendos Inuembles',
                'permissions': [('activate_lease_realty', 'Can activate lease realty.')],
            },
            bases=('accountables.accountable',),
        ),
        migrations.CreateModel(
            name='Date_Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('date', models.DateField(verbose_name='Fecha')),
                ('value', models.PositiveIntegerField(verbose_name='Valor')),
                ('accountable', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='date_value', related_query_name='dates_values', to='accountables.accountable', verbose_name='Contabilizable')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Fecha Valor',
                'verbose_name_plural': 'Fechas Valores',
            },
        ),
        migrations.CreateModel(
            name='Accountable_Transaction_Type',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='Nombre')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transacción Tipo',
                'verbose_name_plural': 'Transacciones Tipos',
                'permissions': [('activate_transaction_type', 'Can activate transaction type.')],
            },
        ),
        migrations.CreateModel(
            name='Accountable_Concept',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('code', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='Código')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('accountable', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='accountable_concept', related_query_name='accountable_concepts', to='accountables.accountable', verbose_name='Contabilizable')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='accountable_concept', related_query_name='accountable_concepts', to='accountables.accountable_transaction_type', verbose_name='Tipo Transacción')),
            ],
            options={
                'verbose_name': 'Concepto Movimiento',
                'verbose_name_plural': 'Conceptos Movimientos',
            },
        ),
        migrations.AddField(
            model_name='accountable',
            name='transaction_types',
            field=models.ManyToManyField(related_name='accountables', related_query_name='accountable', to='accountables.Accountable_Transaction_Type', verbose_name='Tipos de Cargo'),
        ),
        migrations.CreateModel(
            name='Lease_Realty_Realty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('primary', models.BooleanField(verbose_name='Primario')),
                ('realty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='properties.realty', verbose_name='Inmueble')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('lease', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accountables.lease_realty', verbose_name='Contrato')),
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
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('role', models.PositiveSmallIntegerField(choices=[(0, 'Arrendador'), (1, 'Arrendatario'), (2, 'Fiador'), (3, 'Arrendador Titular')], verbose_name='Rol')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='leases_realties_people', related_query_name='lease_realty_person', to='references.address', verbose_name='Dirección')),
                ('e_mail', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='leases_realties_people', related_query_name='lease_realty_person', to='references.e_mail', verbose_name='Correo Electrónico')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.person', verbose_name='Persona')),
                ('phone', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='leases_realties_people', related_query_name='lease_realty_person', to='references.phone', verbose_name='Teléfono')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('lease', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accountables.lease_realty', verbose_name='Contrato')),
            ],
            options={
                'verbose_name': 'Parte Arriendo Inmueble',
                'verbose_name_plural': 'Partes Arriendos Inmuebles',
            },
        ),
        migrations.AddField(
            model_name='lease_realty',
            name='part',
            field=models.ManyToManyField(related_name='leases_realties', related_query_name='lease_realty', through='accountables.Lease_Realty_Person', to='people.Person', verbose_name='Parte'),
        ),
        migrations.AddField(
            model_name='lease_realty',
            name='realty',
            field=models.ManyToManyField(related_name='leases_realties', related_query_name='lease_realty', through='accountables.Lease_Realty_Realty', to='properties.Realty', verbose_name='Inmueble'),
        ),
        migrations.AddConstraint(
            model_name='date_value',
            constraint=models.UniqueConstraint(fields=('accountable', 'date'), name='unique_accountable_date'),
        ),
    ]
