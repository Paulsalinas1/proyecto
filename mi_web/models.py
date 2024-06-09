from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class producto(models.Model):
    nombre=models.CharField(max_length=50, null=False)
    stock=models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(300)])
    descripción=models.CharField(max_length=50, null=False) 
    precio=models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(300)])
    foto=models.ImageField(upload_to='producto',null=False)
    
