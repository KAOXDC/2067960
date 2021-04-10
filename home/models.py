from django.db import models

# Create your models here.

class Categoria (models.Model):
    nombre = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombre
    
class Marca (models.Model):
    nombre = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombre

class Producto (models.Model):
    nombre      = models.CharField(max_length = 100)
    descripcion = models.TextField(max_length = 500)
    precio      = models.DecimalField(max_digits = 9, decimal_places=3 )  # 150000.000 - 9999.99
    cantidad    = models.IntegerField()
    activo      = models.BooleanField(default = True)
    foto        = models.ImageField(upload_to = 'productos', null=True, blank=True)
    marca       = models.ForeignKey(Marca, models.PROTECT)
    categorias  = models.ManyToManyField(Categoria, null=True, blank=True )

    def __str__(self):
        return self.nombre + str(self.precio) 
    