# Generated by Django 3.0.6 on 2020-05-30 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbol', '0012_auto_20200529_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='altitud',
            field=models.FloatField(verbose_name='Altitud'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='latitud',
            field=models.FloatField(verbose_name='Latitud'),
        ),
    ]
