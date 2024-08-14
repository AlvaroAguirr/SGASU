# Generated by Django 5.0.6 on 2024-08-14 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horario', '0004_alter_schedule_se_day'),
        ('salas', '0008_alter_roomtype_rm_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='se_classroom',
        ),
        migrations.AddField(
            model_name='schedule',
            name='se_classroom',
            field=models.ManyToManyField(to='salas.classroom'),
        ),
    ]