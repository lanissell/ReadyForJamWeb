from django.db import models
from tinymce.models import HTMLField


class Jam(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    theme = models.CharField(max_length=128, blank=False, null=False, unique=True)
    content = HTMLField(blank=False, null=False, default='')
    avatar = models.ImageField(upload_to='media/jam/avatar')


class JamForeign:
    jam = models.ForeignKey(Jam, blank=False, null=False, unique=True, on_delete=models.CASCADE)


class JamDate(models.Model, JamForeign):
    startDate = models.DateField(blank=False, null=False)
    votingStartDate = models.DateField(blank=False, null=False)
    votingEndDate = models.DateField(blank=False, null=False)


class JamCriteria(models.Model, JamForeign):
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
