import email
from django.db import models
from django.forms import CharField

# Create your models here.

class Data(models.Model):
    def __str__(self):
        return self.username
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    intro = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    school = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    codeforces = models.CharField(max_length=20)
    codechef = models.CharField(max_length=20)
    leetcode = models.CharField(max_length=20)
    github = models.CharField(max_length=20)
    projects = models.CharField(max_length=500)
    skills = models.CharField(max_length=200)
    achievement = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)