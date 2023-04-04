from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from registration.models import User


class Jam(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    theme = models.CharField(max_length=128, blank=False, null=False)
    avatar = models.ImageField(upload_to='jam/avatar')
    content = RichTextUploadingField(default='', blank=False, null=False,)

class JamDate(models.Model):
    jam = models.ForeignKey(Jam, blank=False, null=False, on_delete=models.CASCADE)
    startDate = models.DateTimeField(blank=False, null=False)
    votingStartDate = models.DateTimeField(blank=False, null=False)
    votingEndDate = models.DateTimeField(blank=False, null=False)

class JamColor(models.Model):
    jam = models.ForeignKey(Jam, blank=False, null=False, on_delete=models.CASCADE)
    backgroundColor = models.CharField(max_length=10, blank=False, null=False)
    formColor = models.CharField(max_length=10, blank=False, null=False)
    mainTextColor = models.CharField(max_length=10, blank=False, null=False)

class JamCriteria(models.Model):
    jam = models.ForeignKey(Jam, blank=False, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)

class Participant(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    jam = models.ForeignKey(Jam, blank=False, null=False, on_delete=models.CASCADE)
    isTeam = models.BooleanField(blank=False, null=False, default=True)

class Project(models.Model):
    participant = models.ForeignKey(Participant, blank=False, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    description = RichTextUploadingField(default='', blank=False, null=False,)
    link = models.CharField(max_length=512, blank=False, null=False, unique=True)