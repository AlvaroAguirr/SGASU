# Generated by Django 5.0.6 on 2024-07-10 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0003_alter_solicitudes_fecha'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Solicitudes',
            new_name='Requests',
        ),
        migrations.RenameField(
            model_name='requests',
            old_name='fecha',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='requests',
            old_name='matricula',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='requests',
            old_name='motivo',
            new_name='reason',
        ),
        migrations.RenameField(
            model_name='requests',
            old_name='nombre',
            new_name='school_enrollment',
        ),
    ]
