# Generated by Django 3.0.6 on 2020-05-22 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arbol', '0003_arbol_direction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arbol',
            old_name='value',
            new_name='carac',
        ),
    ]
