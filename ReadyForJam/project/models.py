from django.contrib.auth.models import User
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from jam.models import Participant, JamCriteria


class Project(models.Model):
    participant = models.OneToOneField(Participant, blank=False, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    avatar = models.ImageField(upload_to='jam/project/avatar', default='')
    content = CKEditor5Field(config_name='extends')

class ProjectColor(models.Model):
    project = models.ForeignKey(Project, blank=False, null=False, on_delete=models.CASCADE)
    background_color = models.CharField(max_length=10, blank=False, null=False)
    form_color = models.CharField(max_length=10, blank=False, null=False)
    main_text_color = models.CharField(max_length=10, blank=False, null=False)

class Vote(models.Model):
    project = models.ForeignKey(Project, blank=False, null=False, on_delete=models.CASCADE)
    criteria = models.ForeignKey(JamCriteria, blank=False, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, default='')
