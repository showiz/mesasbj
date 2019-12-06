from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre_cat = models.CharField(verbose_name="Nombre cat", max_length=255, null=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    def __str__(self):
        return self.nombre_cat


class Mesa(models.Model):
    nombre_mesa = models.CharField(verbose_name="Nombre mesa", max_length=255, null=True)
    cantidad_asientos = models.IntegerField(verbose_name = "Cantidad asientos", null=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    def __str__(self):
        return self.nombre_mesa