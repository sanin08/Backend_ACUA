# Generated by Django 3.0.6 on 2020-05-21 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbol', '0002_auto_20200521_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='arbol',
            name='direction',
            field=models.CharField(default='no hay datos', max_length=200, verbose_name='direccion'),
            preserve_default=False,
        ),
    ]
