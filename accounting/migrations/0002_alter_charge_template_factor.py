# Generated by Django 4.0.2 on 2022-04-13 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0003_alter_charge_factor_options_and_more'),
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge_template',
            name='factor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='charges_templates', related_query_name='charge_template', to='references.charge_factor', verbose_name='Tasa'),
        ),
    ]