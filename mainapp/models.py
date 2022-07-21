from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Postman(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="avatar1.jpg", null=True, blank=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    postman = models.ForeignKey(Postman, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0,
                                validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(0),
                                ])
    def __str__(self):
        return str(self.title)

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=30)
    publisher_title = models.CharField(max_length=200, default="")
    country = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    postman = models.ForeignKey(Postman, on_delete = models.CASCADE, null=True)
    def __str__(self):
        return str(self.publisher_name)

