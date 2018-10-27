from django.db import models

# Create your models here.


class Raza(models.Model):
    nombre = models.CharField(max_length=50)    

    def __str__(self):
        return self.nombre



class Estado(models.Model):
    nombre = models.CharField(max_length=50)
    

    def __str__(self):
        return self.nombre

class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    

class Ciudad(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Tipo_vivienda(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre


class Postulante(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nac = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    tipo_vivienda = models.ForeignKey(Tipo_vivienda, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.nombre
    
    

class Mascotas(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    fecha_ingreso = models.CharField(max_length=50)
    fecha_nacimiento = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)   
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    imagen = models.ImageField(blank=True)

    def __str__(self):
        return self.nombre

    class meta:
        verbose_name ="Mascota"
        verbose_name_plutal="Mascotas"

