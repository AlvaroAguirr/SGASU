# Generated by Django 5.0.6 on 2024-06-26 18:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudes',
            name='fecha',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='Fecha'),
        ),
    ]
