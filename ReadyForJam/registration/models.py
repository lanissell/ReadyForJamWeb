from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    about = models.CharField(max_length=512)
    birthDate = models.DateField(blank=False, null=False)


class UserPhoto(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user/avatar')
    background = models.ImageField(upload_to='user/background')


class Right(models.Model):
    name = models.CharField(max_length=16, blank=False, null=False)
    defaultState = models.BooleanField(default=False)


class UserRight(models.Model):
    right = models.ForeignKey(Right, blank=False, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=False)
