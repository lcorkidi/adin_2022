# Generated by Django 4.0.2 on 2022-03-03 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='total_area',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Área'),
        ),
    ]
