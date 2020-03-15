from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


# Create your models here.

class ProyectoRegresionMultiple(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    objetivos = models.TextField()
    moderador = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='moderador_regresion_multiple',
                                  related_name='regresion_multiple_moderador')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_inicio = models.DateTimeField(default=now)
    fecha_final = models.DateTimeField(default=now)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return "Nombre Proyecto: " + self.titulo


class Fila(models.Model):
    valor = models.FloatField()
    numero_fila = models.PositiveIntegerField()

    def __str__(self):
        return "Numero Fila: " + self.numero_fila + " - Valor Fila: " + self.valor


class Variable(models.Model):
    label = models.CharField(max_length=128)
    nombre = models.CharField(max_length=10)
    filas = models.ManyToManyField(Fila)

    def __str__(self):
        return "Pregunta: " + self.label + " - Nombre Variable: " + self.nombre


class Estudio(models.Model):
    proyecto = models.ForeignKey(ProyectoRegresionMultiple, on_delete=models.CASCADE,
                                 verbose_name='estudio_regresion_multiple',
                                 related_name='regresion_multiple_estudio')
    titulo = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    completado = models.BooleanField(default=False)
    variable_dependiente = models.ForeignKey(Variable, related_name='regresion_multiple_variable_dependiente')
    variables_independientes = models.ManyToManyField(Variable,
                                                      related_name='regresion_multiple_variables_dependientes')

    def __str__(self):
        return "Nombre Proyecto: " + self.proyecto + " - Titulo Estudio: " + self.titulo
