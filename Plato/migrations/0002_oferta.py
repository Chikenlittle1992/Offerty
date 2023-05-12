# Generated by Django 4.2.1 on 2023-05-12 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Plato', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('plato_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Plato.plato')),
                ('fecha_limite', models.DateField()),
            ],
            bases=('Plato.plato',),
        ),
    ]