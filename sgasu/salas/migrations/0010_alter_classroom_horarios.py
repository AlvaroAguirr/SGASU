# Generated by Django 5.0.7 on 2024-08-14 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horario', '0006_remove_schedule_se_classroom'),
        ('salas', '0009_classroom_horarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='horarios',
            field=models.ManyToManyField(related_name='salones', to='horario.schedule'),
        ),
    ]