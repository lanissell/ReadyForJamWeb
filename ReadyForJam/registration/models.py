from django.db import models


class User(models.Model):
    login = models.CharField(max_length=128, blank=False, null=False, unique=True)
    password = models.CharField(max_length=24, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    about = models.CharField(max_length=512)
    birthDate = models.DateField(blank=False, null=False)
    dateCreate = models.DateField(auto_now_add=True)
    isBlocked = models.BooleanField(default=False)


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
