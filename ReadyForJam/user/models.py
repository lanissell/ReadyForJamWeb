from django.db import models


class User(models.Model):
    NickName = models.CharField(max_length=255, blank=False, null=False)
    Rate = models.IntegerField(default=0, blank=False, null=False)
    IsLeader = models.BooleanField(default=False, blank=False, null=False)
    TeamId = models.IntegerField(default=0, blank=False, null=False)
    AvatarUrl = models.ImageField(blank=False, null=False, upload_to='user/avatar')
    Password = models.CharField(max_length=255, default="*",
                                blank=False, null=False,)

