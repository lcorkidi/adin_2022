# Generated by Django 4.0.2 on 2022-03-24 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('references', '0001_initial'),
        ('accountables', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('code', models.PositiveBigIntegerField(primary_key=True, serialize=False, verbose_name='Código')),
                ('name', models.CharField(blank=True, max_length=128, verbose_name='Nombre')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cuenta',
                'verbose_name_plural': 'Cuentas',
                'permissions': [('activate_account', 'Can activate account.')],
            },
        ),
        migrations.CreateModel(
            name='Ledger_Type',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='Nombre')),
                ('abreviation', models.CharField(max_length=4, verbose_name='Abreviación')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Registro Tipo',
                'verbose_name_plural': 'Registros Tipos',
            },
        ),
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('code', models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='Código')),
                ('consecutive', models.PositiveIntegerField(verbose_name='Consecutivo')),
                ('description', models.TextField(blank=True, default=None, max_length=255, null=True, verbose_name='Descripción')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('holder', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ledgers_holders', related_query_name='ledger_holder', to='people.person', verbose_name='Titular')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('third_party', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ledgers_third_parties', related_query_name='ledger_third_party', to='people.person', verbose_name='Tercero')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ledgers', related_query_name='ledger', to='accounting.ledger_type', verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
            },
        ),
        migrations.CreateModel(
            name='Charge_Concept',
            fields=[
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('code', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='Código')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('accountable', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='charges_concepts', related_query_name='charge_concept', to='accountables.accountable', verbose_name='Contabilizable')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='charges_concepts', related_query_name='charge_concept', to='references.transaction_type', verbose_name='Tipo Transacción')),
            ],
            options={
                'verbose_name': 'Concepto Movimiento',
                'verbose_name_plural': 'Conceptos Movimientos',
            },
        ),
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_change_date', models.DateTimeField(auto_now=True)),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Por Correguir'), (2, 'Por Revisar'), (3, 'Revisado')], default=1)),
                ('value', models.IntegerField(verbose_name='Valor')),
                ('settled', models.BooleanField(verbose_name='Cruzado')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='charges', related_query_name='charge', to='accounting.account', verbose_name='Cuenta')),
                ('concept', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='charges', related_query_name='charge', to='accounting.charge_concept')),
                ('ledger', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='charges', related_query_name='charge', to='accounting.ledger', verbose_name='Registro')),
                ('state_change_user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Movimiento',
                'verbose_name_plural': 'Movimientos',
            },
        ),
        migrations.AddConstraint(
            model_name='ledger',
            constraint=models.UniqueConstraint(fields=('type', 'consecutive'), name='unique_type_consecutive'),
        ),
    ]
