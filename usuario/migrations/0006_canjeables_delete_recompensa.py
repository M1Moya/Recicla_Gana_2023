# Generated by Django 4.2.7 on 2023-11-13 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_alter_recompensa_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canjeables',
            fields=[
                ('id_recom', models.IntegerField(db_column='Id_Recompensa', primary_key=True, serialize=False)),
                ('recompensa', models.CharField(db_column='Recompensa', max_length=40)),
                ('puntos', models.IntegerField(db_column='Puntos')),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Recompensa',
        ),
    ]
