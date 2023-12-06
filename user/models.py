from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UsuarioManager(BaseUserManager):
    def _create_user(self, rut, email, nombre, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            rut = rut,
            email = email,
            nombre = nombre,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, email, rut, nombre, password = None, **extra_fields):
        return self._create_user(rut, email, nombre, password, False, False, **extra_fields)
    
    def create_superuser(self, rut, email, nombre, password= None, **extra_fields):
        return self._create_user(rut, email, nombre, password, True, True, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    rut = models.CharField("Rut", primary_key=True, max_length=12)    
    password = models.CharField("Contraseña", max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField("Nombre",max_length=150, null=False)
    apellido = models.CharField("Apellido",max_length=150, null=False)
    email = models.CharField(unique=True , max_length=254, null=False)
    is_staff = models.BooleanField(default=False,)
    is_active = models.BooleanField(default=True)
    puntos = models.IntegerField("Puntos", blank=True, null=True)
    objects = UsuarioManager()

    USERNAME_FIELD = "rut"
    REQUIRED_FIELDS = ['email', 'nombre']

    def __str__(self):
        return f'{self.rut}, {self.nombre}, {self.apellido}'
    
