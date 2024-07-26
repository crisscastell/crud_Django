from django.db import models

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    anio = models.IntegerField()
    Protagonista = models.CharField(max_length=100)
    class Meta:
        db_table = 'peliculas'

    def __str__(self):
        return self.titulo
