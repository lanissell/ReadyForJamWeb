from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm
from django import forms

from globalUtils import BasicHtmlAttrs
from jam.forms import JamColorForm
from project.models import Project, ProjectColor


class JamProjectRegisterForm(ModelForm):
    attrs = BasicHtmlAttrs.inputFieldAttrs

    name = forms.CharField(label='Название', widget=forms.TextInput(
        attrs=attrs
    ))
    avatar = forms.ImageField(label='Аватар', widget=forms.FileInput(
        attrs=attrs
    ))
    content = forms.Field(label='Описание',
                          widget=CKEditorWidget())

    class Meta:
        model = Project
        fields = ['name', 'avatar', 'content']

class ProjectColorForm(JamColorForm):
    class Meta:
        model = ProjectColor
        fields = ['background_color', 'form_color', 'main_text_color']