from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class Student(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    age=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=30)



class Stud_details(models.Model):
    stud_id=models.BigAutoField(primary_key=True)
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    age=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=30)




class User(AbstractUser):
    usertype=models.CharField(max_length=50)
    phone=models.BigIntegerField(default=1)


class Employee(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    age=models.IntegerField()
    email=models.EmailField(max_length=30)
    phone=models.BigIntegerField()
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=20)

class stud_user(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    department=models.CharField(max_length=3)
    plus_mark=models.IntegerField()

