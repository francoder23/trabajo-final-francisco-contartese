from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
       return self.nombre
    
    class Meta:
       verbose_name = "país"
       verbose_name_plural = "países"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    nacimiento = models.DateField(null=True, blank=True)
    pais_origen_fk = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="pais de origen")

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
class Meta:
    verbose_name = "estudiante"
    verbose_name_plural = "estudiantes"