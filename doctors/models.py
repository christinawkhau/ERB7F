from django.db import models
from datetime import datetime

# Create your models here.

class Doctor(models.Model):
    name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='photos/%Y/%x/%d/')
    description=models.TextField(blank=True) 
    email=models.EmailField(max_length=50, unique=True, blank=False)
    is_mvp=models.BooleanField(default=True)
    hire_date=models.DateTimeField(auto_now_add=True) #automatically fill in date time
   
    def __str__(self):      #python internal variable
        return self.name
    