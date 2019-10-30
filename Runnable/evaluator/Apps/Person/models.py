from django.db import models
from Apps.Jury.models import Jury 
# Create your models here.
class Person(models.Model):
    primary_key = True
    nombre = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    jury = models.ManyToManyField(Jury)
