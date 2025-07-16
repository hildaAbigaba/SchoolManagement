from django.db import models

# Create your models here.
class Student(models.Model):
    names = models.CharField(max_length=255)
    course = models.TextField()
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    result = models.IntegerField()
    gender = models.CharField(max_length=10) #Male or Female
    student_id = models.CharField(max_length=15) #ST0001

#You need to migrate after creating your models but you need to first recheck because you need to restart
# Processes of migrate
# py manage.py makemigrations (an application name) - It generates the files needed for migrations /If you dont do this , django might skip this model
# py manage.py migrate (this actually migrates) 
