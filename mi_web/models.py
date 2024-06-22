from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class producto(models.Model):
    nombre=models.CharField(max_length=50, null=False ,unique=True)
    stock=models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(1000)])
    descripción=models.CharField(max_length=50, null=False) 
    precio=models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(999999)])
    foto=models.ImageField(upload_to='producto',null=False)
    
    def __str__(self):
        return f"{self.nombre}"
