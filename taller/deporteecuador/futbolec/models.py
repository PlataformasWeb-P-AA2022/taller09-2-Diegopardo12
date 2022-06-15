from django.db import models
from requests import delete

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=30)
    user_twiiter = models.CharField(max_length=50) 

    def __str__(self):
        return "%s - %s - %s - " % (self.nombre, self.siglas, self.user_twiiter)

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion_campo = models.CharField(max_length=50)
    numero_camiseta = models.IntegerField()
    sueldo = models.IntegerField()
    equipo_fut = models.ForeignKey(Equipo, related_name= 'equipos',
        on_delete= models.CASCADE)

    def __str__(self):
        return "%s - %s - %d - %d -%s" % (self.nombre, 
            self.posicion_campo,
            self.numero_camiseta,
            self.sueldo,
            self.equipo_fut)

class Campeonato(models.Model):
    nombre_camp = models.CharField(max_length=100)
    auspiciante = models.CharField(max_length=100)

    def __str__(self):
        return "%s - %s" % (self.nombre_camp,
        self.auspiciante)

class Campeonatodeequipo(models.Model):
    anio = models.IntegerField()
    equipo_fut = models.ForeignKey(Equipo, related_name= 'campeonatos',
        on_delete= models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name= 'campeonatos',
        on_delete= models.CASCADE)

    def __str__(self):
        return "Ficha: %s - Equipo(%s) - Campeonato(%s)" % (
            self.anio,
            self.equipo_fut.nombre,
            self.campeonato.nombre_camp)