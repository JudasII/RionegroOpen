from pickle import FALSE
from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class Competitor(models.Model):
    nombres= models.CharField(max_length=50,blank= True)
    apellidos= models.CharField(max_length=50,blank= True )
    documento = models.IntegerField(blank= True )
    genero = models.CharField(max_length=50,blank= True )
    academia= models.CharField(max_length=50,blank= True )
    cinturon = models.CharField(max_length=50,blank= True )
    pais = models.CharField(max_length=50,blank= True )
    ciudad = models.CharField(max_length= 50,blank= True )
    fechaNacimiento= models.CharField(max_length= 50, blank= True )
    edad=  models.IntegerField(blank= True )
    categoriaEdad= models.CharField(max_length=50,blank= True )
    categoriaPeso= models.CharField(max_length=50,blank= True )
    comprobantePago = models.ImageField(upload_to= 'media/comprobantes/',blank= True)
    verificado= models.BooleanField(default=False)

    @property
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.comprobantePago.url))

    