from django.db import models
from django.forms import forms
from django.contrib.auth.models import User
# Create your models here.
class BrandModel(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True,blank=True,null=True)
    def __str__(self):
       return self.name
class CarModel(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200000000)
    quantity=models.IntegerField()
    price= models.DecimalField(max_digits=10, decimal_places=2)
    brand_name=models.ForeignKey(BrandModel,on_delete=models.CASCADE,related_name='CarModel')
    image=models.ImageField(upload_to='image/uploads')
    def __str__(self):
        return self.name
class Buy(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Buy')
    car=models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name='Buy')
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.car.name
class commnetsModel(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='commentsModel')
    user_name=models.CharField(max_length=100)
    email=models.EmailField()
    body=models.TextField()

   


    
    