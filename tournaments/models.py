from django.db import models

# Create your models here.
class Tournament(models.Model):
    tittle = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')