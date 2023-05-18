from django.forms import ModelForm
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from globalUtils import BasicHtmlAttrs
from jam.forms import JamColorForm
from project.models import Project, ProjectColor


class JamProjectRegisterForm(ModelForm):
    attrs = BasicHtmlAttrs.inputFieldAttrs

    name = forms.CharField(label='Название', widget=forms.TextInput(
        attrs=attrs
    ), required=False)
    avatar = forms.ImageField(label='Аватар', widget=forms.FileInput(
        attrs=attrs
    ))
    content = forms.CharField(label='Описание', required=False, widget=CKEditor5Widget(
        attrs={'class': 'django_ckeditor_5'}, config_name="extends",
    ))

    class Meta:
        model = Project
        fields = ['name', 'avatar', 'content']


class ProjectColorForm(JamColorForm):
    class Meta:
        model = ProjectColor
        fields = ['background_color', 'form_color', 'main_text_color']
