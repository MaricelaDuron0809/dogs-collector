from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dog(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_dog = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Treat(models.Model):

    name = models.CharField(max_length=150)
    length = models.IntegerField(default=0)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name="treats")

    def __str__(self):
        return self.name

class Pawll(models.Model):

    name = models.CharField(max_length=150)
    dogs = models.ManyToManyField(Dog)

    def __str__(self):
        return self.name
