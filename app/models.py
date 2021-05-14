from django.db import models
from multiselectfield import MultiSelectField

MY_CHOICES = (('Mon', 'Monday'),
              ('Tue', 'Tuesday'),
              ('Wed', 'Wednesday'),
              ('Thu', 'Thursday'),
              ('Fri', 'Friday'),
              ('Sat', 'Saturday'),
              ('Sun', 'Sunday'))

# Create your models here.
class DocLogin(models.Model):
    dname = models.CharField(max_length=30)
    dpass = models.CharField(max_length=30)

class DocDetails(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    about = models.CharField(max_length=1024)
    image = models.FileField()
    studies = models.CharField(max_length=30)
    date = MultiSelectField(choices=MY_CHOICES)

class Sign(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phn = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Patients(models.Model):
    ida = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phn = models.CharField(max_length=30)
    dob = models.DateField(max_length=30)
    date = models.DateField(default=False)
    start = models.TimeField(max_length=30)
    end = models.TimeField(max_length=30)
    sym = models.TextField(max_length=100)
    pres = models.TextField(max_length=1024)

class Comments(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    comments = models.TextField(max_length=100)