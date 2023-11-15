# Generated by Django 4.2.7 on 2023-11-13 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_rename_materialesreciclables_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recompensa',
            fields=[
                ('id_recom', models.IntegerField(db_column='Id_Recompensa', primary_key=True, serialize=False)),
                ('recompensa', models.CharField(db_column='Recompensa', max_length=40)),
                ('puntos', models.IntegerField(db_column='Puntos')),
            ],
            options={
                'db_table': 'Recompensas',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'managed': False},
        ),
    ]