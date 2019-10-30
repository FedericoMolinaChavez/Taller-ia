from django.db import models

# Create your models here.
class Jury(models.Model):
    primary_key = True
    nombre = models.CharField(max_length=50)
    fechaSubida = models.DateField()
    archivo = models.TextField()
    resultados = models.TextField()