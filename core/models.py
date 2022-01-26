from django.db import models

# Create your models here.


class Raza(models.Model):
    idRaza = models.AutoField(primary_key=True, verbose_name='Id Raza')
    nombreRaza = models.CharField(max_length=50, verbose_name='Nombre Categoría')

    def __str__(self):
        return self.nombreRaza


class Persona(models.Model):
    rut = models.CharField(max_length=12, primary_key=True, verbose_name='Rut adoptador')
    pnombre = models.CharField(max_length=20, verbose_name='Primer nombre')
    snombre = models.CharField(max_length=20, verbose_name='Segundo nombre')
    papellido = models.CharField(max_length=20, verbose_name='Primer apellido')
    sapellido = models.CharField(max_length=20, verbose_name='Segundo apellido')
    edad = models.CharField(max_length=2, verbose_name='Edad')
    telefono = models.CharField(max_length=12, verbose_name='Telefono')
    email = models.CharField(max_length=30, verbose_name='Email')
    contrasena = models.CharField(max_length=20, verbose_name='Contrasena')

    def __str__(self):
        return self.rut


class Gato(models.Model):
    id_chip = models.CharField(max_length=8, primary_key=True, verbose_name='Chip')
    nombre = models.CharField(max_length=20, verbose_name='Nombre gato')
    color = models.CharField(max_length=20, verbose_name='Color gato')
    sexo = models.CharField(max_length=20, verbose_name='Sexo')
    edad = models.CharField(max_length=2, verbose_name='Edad de gato')
    Descripcion = models.CharField(max_length=1000, verbose_name='Descripción del gato')
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    rut = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_chip 
        
        
