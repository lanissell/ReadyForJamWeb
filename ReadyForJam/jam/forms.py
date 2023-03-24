from django.forms import ModelForm
from django import forms
from tinymce.widgets import TinyMCE

from jam.models import Jam
from registration.utils import BasicHtmlAttrs


class JamRegistrationForm(ModelForm):
    attrs = BasicHtmlAttrs.inputFieldAttrs

    name = forms.CharField(label='Название', widget=forms.TextInput(
        attrs=attrs
    ))
    theme = forms.CharField(label='Тема', widget=forms.TextInput(
        attrs=attrs
    ))
    content = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Jam
        fields = ['name', 'theme', 'content']

