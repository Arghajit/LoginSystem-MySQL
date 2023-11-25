from django.db import models


#created three user levels-Superadmin,Teacher,Student
class User(models.Model):
    id=models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=30,default="")
    lastname = models.CharField(max_length=30,default="")
    picture=models.ImageField(upload_to='images')
    username = models.CharField(max_length=30,default="")
    email = models.CharField(max_length=30,default="")
    password = models.CharField(max_length=30,default="")
    address = models.CharField(max_length=30,default="")
    type = models.CharField(max_length=30,default="")

    def __str__(self):
        return self.username
    

# Create your models here.
