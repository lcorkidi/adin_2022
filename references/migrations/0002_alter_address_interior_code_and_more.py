# Generated by Django 4.0.2 on 2022-03-09 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='interior_code',
            field=models.CharField(blank=True, default=None, max_length=6, null=True, verbose_name='Interior Código'),
        ),
        migrations.AlterField(
            model_name='address',
            name='interior_group_code',
            field=models.CharField(blank=True, default=None, max_length=6, null=True, verbose_name='Interior Grupo Código'),
        ),
    ]
