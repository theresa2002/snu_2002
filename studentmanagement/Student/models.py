from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    usertype=models.CharField(max_length=20)
    phone=models.BigIntegerField(default=1)



class Student_User(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    department=models.CharField(max_length=15)
    plus_mark=models.IntegerField()
