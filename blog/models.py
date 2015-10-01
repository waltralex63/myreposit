from django.db import models
from django.utils import timezone

class Postear(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creada = models.DateTimeField(
            default=timezone.now)
    fecha_publicada = models.DateTimeField(
            blank=True, null=True)

    def publicacion(self):
        self.fecha_publicada = timezone.now()
        self.save()
    def __str__(self):
        return self.titulo
