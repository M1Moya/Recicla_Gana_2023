# Generated by Django 4.2.7 on 2023-11-15 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_usuario_fecha_nac'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_nac',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='genero',
        ),
    ]
