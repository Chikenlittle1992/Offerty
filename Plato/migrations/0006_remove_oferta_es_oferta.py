# Generated by Django 4.1.6 on 2023-05-23 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Plato', '0005_oferta_es_oferta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oferta',
            name='es_oferta',
        ),
    ]
