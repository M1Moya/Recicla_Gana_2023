from django.db import models

# Create your models here.

# Modelo de Materiales Reciclables
class Material(models.Model):
    id_material = models.AutoField(primary_key=True,unique=True, db_column='Id_Material', null=False)
    material = models.CharField(max_length=40, db_column='Material')
    valor_puntos = models.IntegerField(db_column='Valor_Unitario_Puntos')

    class Meta:
        managed = False


    def __str__(self):
        return self.material
    
# Modelo de Recompensas    
class Canjeables(models.Model):
    id_recom = models.AutoField(primary_key=True, unique=True, db_column="Id_Recompensa", null=False)
    recompensa = models.CharField(db_column="Recompensa", max_length=40, null=False)
    puntos = models.IntegerField(db_column="Puntos")
    categoria = models.CharField(db_column="Categoria", max_length=20, default="", null=False)

    def __str__(self):
        return self.recompensa