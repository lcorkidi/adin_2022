# Generated by Django 4.0.2 on 2022-04-13 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0002_alter_charge_factor_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='charge_factor',
            options={'permissions': [('activate_charge_factor', 'Can activate charge factor.')], 'verbose_name': 'Tasa Transacción', 'verbose_name_plural': 'Tasas Transacciones'},
        ),
        migrations.AlterModelOptions(
            name='factor_data',
            options={'verbose_name': 'Datos Tasas', 'verbose_name_plural': 'Datos Tasas'},
        ),
        migrations.AlterField(
            model_name='factor_data',
            name='amount',
            field=models.PositiveIntegerField(default=0, verbose_name='Monto'),
        ),
        migrations.AlterField(
            model_name='factor_data',
            name='factor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='datas', related_query_name='data', to='references.charge_factor', verbose_name='Tasa'),
        ),
        migrations.AlterField(
            model_name='factor_data',
            name='percentage',
            field=models.DecimalField(decimal_places=3, default=100, max_digits=6, verbose_name='Porcentaje'),
        ),
    ]
