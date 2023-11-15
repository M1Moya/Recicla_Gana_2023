from django.db import models

# Create your models here.
class Material(models.Model):
    id = models.CharField(primary_key=True, max_length=5, db_column='Id_Material')
    material = models.CharField(max_length=40, db_column='Material')
    valor_puntos = models.IntegerField(db_column='Valor_Unitario_Puntos')

    class Meta:
        managed = False


    def __str__(self):
        return self.material
    
class Canjeables(models.Model):
    id_recom = models.AutoField(primary_key=True, unique=True, db_column="Id_Recompensa", null=False)
    recompensa = models.CharField(db_column="Recompensa", max_length=40, null=False)
    puntos = models.IntegerField(db_column="Puntos")
    categoria = models.CharField(db_column="Categoria", max_length=20, default="", null=False)

    def __str__(self):
        return self.recompensa