# Generated by Django 4.1.2 on 2023-04-30 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0005_rename_es_consumidor_user_is_consumidor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_Consumidor',
            new_name='is_cestaurante',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_Restaurante',
        ),
        migrations.AddField(
            model_name='user',
            name='is_consumidor',
            field=models.BooleanField(default=False),
        ),
    ]
