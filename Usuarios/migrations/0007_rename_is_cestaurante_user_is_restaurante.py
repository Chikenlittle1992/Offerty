# Generated by Django 4.1.2 on 2023-04-30 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0006_rename_is_consumidor_user_is_cestaurante_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_cestaurante',
            new_name='is_restaurante',
        ),
    ]
