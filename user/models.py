from django.contrib.auth.models import User
from django.db import models


class FamousPeople(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    avatar_1 = models.ImageField(upload_to='media/images/famous_people/', blank=False, null=False)
    avatar_2 = models.ImageField(upload_to='media/images/famous_people/', blank=True, null=True)
    avatar_3 = models.ImageField(upload_to='media/images/famous_people/', blank=True, null=True)
    video = models.FileField(upload_to='media/videos/famous_people/', blank=False, null=False)
    review = models.TextField()

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class Adminstrator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    avatar = models.ImageField(upload_to='media/images/adminstrator/', blank=False, null=False)
    phone = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.user.username
