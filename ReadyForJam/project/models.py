from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from jam.models import Participant


class Project(models.Model):
    participant = models.OneToOneField(Participant, blank=False, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    avatar = models.ImageField(upload_to='jam/project/avatar', default='')
    content = RichTextUploadingField(default='', blank=False, null=False,)

class ProjectColor(models.Model):
    project = models.ForeignKey(Project, blank=False, null=False, on_delete=models.CASCADE)
    background_color = models.CharField(max_length=10, blank=False, null=False)
    form_color = models.CharField(max_length=10, blank=False, null=False)
    main_text_color = models.CharField(max_length=10, blank=False, null=False)
