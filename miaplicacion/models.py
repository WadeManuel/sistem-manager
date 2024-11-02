from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Rol(models.Model):
    nombre=models.CharField(max_length=255,blank=False)

class Usuario(AbstractUser):
    createAt = models.DateField(auto_now_add = True)
    rol = models.ForeignKey(Rol, on_delete = models.CASCADE, null = False)
    email = models.EmailField(max_length = 255, blank = False, unique = True)

class Vendedor(models.Model):
    nombre=models.CharField(max_length=255,blank=False)
    apellidos=models.CharField(max_length=255,blank=False)
    anos_trabajo=models.IntegerField(null=False,blank=False)
    
class Cliente(models.Model):
    nombre = models.CharField(max_length = 255, blank = False)
    direccion = models.CharField(max_length = 255, blank = False)
    telefono = models.IntegerField(null = False, blank = False)
    vendedor = models.ForeignKey(Vendedor, on_delete = models.CASCADE)

class Deportivo(models.Model):
    modelo=models.CharField(max_length=155,blank=False)
    marca=models.CharField(max_length=155,blank=False)
    precio=models.FloatField(null=False)
    kilometraje=models.IntegerField(null=False,blank=False)
    caballos_fuerza=models.IntegerField(null=False,blank=False)
    imagen=models.ImageField(upload_to='imagenes/',default='imagen')
    
class Registro_Compra(models.Model):
    monto=models.FloatField(null=False)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    deportivo=models.ForeignKey(Deportivo,on_delete=models.CASCADE)
    fechaC=models.DateField(auto_now_add=True)