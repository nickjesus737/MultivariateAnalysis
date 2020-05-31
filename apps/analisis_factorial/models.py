from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator


class ProyectoAnalisisFactorial(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    objetivos = models.TextField(blank=True)
    moderador = models.ForeignKey(User, on_delete=models.PROTECT,
                                  verbose_name='moderador_analisis_factorial', related_name='analisis_factorial_moderador')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_inicio = models.DateTimeField(default=now)
    fecha_final = models.DateTimeField(default=now)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return "Nombre Proyecto: " + self.titulo


class Estudio(models.Model):

    VARIMAX = 'variamax'
    PROMAX = 'promax'
    OBLIMIN = 'oblimin'
    OBLIMAX = 'oblimax'
    QUARTIMIN = 'quartimin'
    QUARTIMAX = 'quartimax'
    EQUAMAX = 'equamax'

    ROTACION_METODOS = [
        (VARIMAX, 'Variamax'),
        (PROMAX, 'Promax'),
        (OBLIMIN, 'Oblimin'),
        (OBLIMAX, 'Oblimax'),
        (QUARTIMIN, 'Quartimin'),
        (QUARTIMAX, 'Quartimax'),
        (EQUAMAX, 'Equamax'),
    ]

    proyecto = models.ForeignKey(ProyectoAnalisisFactorial, on_delete=models.CASCADE,
                                 verbose_name='estudio_analisis_factorial', related_name='analisis_factorial_estudio')
    titulo = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    completado = models.BooleanField(default=False)
    numero_componenentes = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)], null=True, blank=True)
    rotacion = models.CharField(
        max_length=10, choices=ROTACION_METODOS, default=VARIMAX)
    archivo_datos = models.FileField(null=True, blank=True)

    def __str__(self):
        return "Nombre Proyecto: " + self.proyecto + " - Titulo Estudio: " + self.titulo
