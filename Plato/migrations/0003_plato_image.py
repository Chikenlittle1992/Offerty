# Generated by Django 4.2.1 on 2023-05-12 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plato', '0002_oferta'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Imagen'),
        ),
    ]
