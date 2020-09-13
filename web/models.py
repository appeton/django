from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
    image=models.ImageField(default="default.jpg",upload_to="picture")
    p_brand=models.CharField(max_length=20)
    p_name=models.CharField(max_length=20)
    price=models.IntegerField()
    size_1=models.IntegerField()
    size_2=models.IntegerField()
    size_3=models.IntegerField()
    size_4=models.IntegerField()
    size_5=models.IntegerField()
    quantity=models.IntegerField()
    gender=models.CharField(max_length=20)



class slider(models.Model):
    image=models.ImageField(upload_to="picture")
    brand=models.CharField(max_length=20)
    percentage=models.CharField(max_length=20)


class order(models.Model):
    productname=models.CharField(max_length=100)
    productsize=models.CharField(max_length=100)
    productquantity=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    Zip=models.CharField(max_length=100)
    userId=models.CharField(max_length=100)



class feedback(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    about=models.CharField(max_length=600)



      



