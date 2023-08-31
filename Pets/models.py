from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class DogBed(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="dog_beds", blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class DogToy(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="dog_toys", blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class DogCollar(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="dog_collars", blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class DogFood(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="dog_foods", blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class CatFood(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="cat_foods", blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class CatToy(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="cat_toys", blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title

