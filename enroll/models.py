from django.db import models
class user(models.Model):
    Name=models.CharField(max_length=70)
    Email=models.EmailField(max_length=100)
    Password=models.CharField(max_length=70)

# Create your models here.
