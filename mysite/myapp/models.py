from django.db import models

# Create your models here.
class Form_1(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField()
  age =  models.IntegerField()
  college = models.CharField(max_length=200)
  rollno =  models.IntegerField()
  year =  models.IntegerField()
  branch =  models.CharField(max_length=200)
  interests = models.TextField()
  def __str__(self):
    return self.name
  

