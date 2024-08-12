# Generated by Django 5.0.6 on 2024-08-12 19:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horario', '0001_initial'),
        ('salas', '0007_classroom_cm_roof'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='se_classroom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='horario_de_salon', to='salas.classroom'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='se_end_time',
            field=models.TimeField(verbose_name='hora de finalizacion'),
        ),
    ]
