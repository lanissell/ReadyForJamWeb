from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from registration.models import User


class Jam(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    theme = models.CharField(max_length=128, blank=False, null=False)
    avatar = models.ImageField(upload_to='jam/avatar')
    content = RichTextUploadingField(default='', blank=False, null=False,)
    author = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE)

class JamDate(models.Model):
    jam = models.ForeignKey(Jam, blank=False, null=False, on_delete=models.CASCADE)
    start_date = models.CharField(max_length=30, blank=False, null=False)
    voting_start_date = models.CharField(max_length=30,blank=False, null=False)
    voting_end_date = models.CharField(max_length=30,blank=False, null=False)
    time_zone = models.CharField(max_length=30,blank=False, null=False, default='Asia/Krasnoyarsk')

class JamColor(models.Model):
    jam = models.ForeignKey(Jam, blank=False, null=False, on_delete=models.CASCADE)
    background_color = models.CharField(max_length=10, blank=False, null=False)
    form_color = models.CharField(max_length=10, blank=False, null=False)
    main_text_color = models.CharField(max_length=10, blank=False, null=False)

class JamCriteria(models.Model):
    jam = models.ForeignKey(Jam, blank=False, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False, null=False, unique=False)

class Participant(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    jam = models.ForeignKey(Jam, blank=False, null=False, on_delete=models.CASCADE)
    is_team = models.BooleanField(blank=False, null=False, default=True)

class Project(models.Model):
    participant = models.ForeignKey(Participant, blank=False, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    description = RichTextUploadingField(default='', blank=False, null=False,)
    link = models.CharField(max_length=512, blank=False, null=False, unique=True)