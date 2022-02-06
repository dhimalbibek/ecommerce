import email
from django.db import models
from django.forms import GenericIPAddressField

Gender =(
    ('m', 'Male'),
    ('f', 'Female'),
    ('o', 'Others')
)

# Create your models here.
class product(models.Model):
    name =models.CharField(max_length=50)
    address =models.CharField(max_length=50)
    price =models.IntegerField()
    image =models.ImageField()
    gender=models.CharField(max_length=1,choices=Gender)
    email =models.EmailField()
    quality=models.CharField(max_length=20)
    phone =models.IntegerField()
    content =models.TextField()
    title=models.CharField(max_length=500)


