from django.db import models

# Create your models here.


class Mobile(models.Model):
    name=models.CharField(max_length=50,primary_key=True)
    description=models.CharField(max_length=50)
    processor=models.CharField(max_length=10)
    ram=models.IntegerField()
    screen_size=models.IntegerField()
    color=models.CharField(max_length=10)

    def __repr__(self):
        return self.name


class Laptop(models.Model):
    name=models.CharField(max_length=50,primary_key=True)
    description=models.CharField(max_length=50)
    processor=models.CharField(max_length=10)
    ram=models.IntegerField()
    hd_capacity=models.BooleanField()

class User(models.Model):
    username=models.CharField(max_length=10)
    password=models.IntegerField()
   

class UserSession(models.Model):
    username=models.CharField(max_length=10)
    password=models.IntegerField()




