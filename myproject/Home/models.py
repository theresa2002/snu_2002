from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    dob=models.DateField()
    age=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=30)

    class meta:
        dbl_table="tabl stud"

class Employee(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    dob=models.DateField()
    age=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=30)
    depart=(
        ("HR",'Humen Resourse'),
        ("CS","Computer Science"),
        ("EE","Electronic Engineer ")

    )
    dep=models.CharField(max_length=2,choices=depart)


class FileUpload(models.Model):
    name=models.CharField(max_length=30)
    file=models.FileField()





   




