# Generated by Django 4.1.2 on 2023-04-30 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0007_rename_is_cestaurante_user_is_restaurante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurante',
            name='id',
        ),
        migrations.AddField(
            model_name='restaurante',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Restaurante', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
