from django.forms import ModelForm
from django import forms

from jam.models import Jam
from registration.utils import BasicHtmlAttrs


class JamRegistrationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # it is required to set it False,
        # otherwise it will throw error in console
        self.fields["content"].required = False

    attrs = BasicHtmlAttrs.inputFieldAttrs

    name = forms.CharField(label='Название', widget=forms.TextInput(
        attrs=attrs
    ))
    theme = forms.CharField(label='Тема', widget=forms.TextInput(
        attrs=attrs
    ))
    color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color', 'class': 'bgColor'}))

    class Meta:
        model = Jam
        fields = ['name', 'theme', 'content']

    field_order = ['name', 'theme', 'color' ,'content']