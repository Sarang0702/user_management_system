from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    phone = models.IntegerField(max_length=12)
    password = models.CharField(max_length=15)

class Teacher(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    phone = models.IntegerField(max_length=12)
    password = models.CharField(max_length=15)

class Institute(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    phone = models.IntegerField(max_length=12)
    password = models.CharField(max_length=15)
