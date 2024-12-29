from django.db import models

# Create your models here.

class Company(models.Model):
    username = models.CharField(max_length=150)
    age=models.IntegerField()
    place=models.CharField(max_length=150)
    email=models.EmailField()
    job=models.CharField(max_length=150)
    image=models.FileField(upload_to='images/',null=True,blank=True)
    password=models.CharField(max_length=150)

    def __str__(self):
        return self.username