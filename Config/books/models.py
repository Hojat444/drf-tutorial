from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    
    owner = models.ForeignKey(User,null = True , blank = True , related_name = "books",on_delete = models.SET_NULL)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title

    
class Writer(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    book = models.ManyToManyField(Book,related_name="writers")
    
    def __str__(self):
        return self.first_name+" "+self.last_name
      