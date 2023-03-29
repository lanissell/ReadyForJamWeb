from datetime import datetime

from django.forms import ModelForm
from django import forms

from jam.models import Jam, JamColor, JamDate
from registration.forms import DateInput
from registration.utils import BasicHtmlAttrs


class JamRegistrationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False

    attrs = BasicHtmlAttrs.inputFieldAttrs

    name = forms.CharField(label='Название', widget=forms.TextInput(
        attrs=attrs
    ))
    theme = forms.CharField(label='Тема', widget=forms.TextInput(
        attrs=attrs
    ))

    class Meta:
        model = Jam
        fields = ['name', 'theme', 'content']

    field_order = ['name', 'theme']

class JamDateForm(ModelForm):

    dateAttrs = {
        'class': BasicHtmlAttrs.inputFieldAttrs['class'],
        'max': f"{datetime.now().year + 20}-12-31",
        'min': "1900-12-31"
    }

    startDate = forms.DateField(label='Дата рождения', widget=DateInput(
        attrs=dateAttrs
    ))
    votingStartDate = forms.DateField(label='Дата рождения', widget=DateInput(
        attrs=dateAttrs
    ))
    votingEndDate = forms.DateField(label='Дата рождения', widget=DateInput(
        attrs=dateAttrs
    ))

    class Meta:
        model = JamDate
        fields = ['startDate', 'votingStartDate', 'votingEndDate']

class JamColorForm(ModelForm):

    backgroundColor = forms.CharField(widget=forms.TextInput(attrs={'type': 'color', 'class': 'bgColor'}))
    formColor = forms.CharField(widget=forms.TextInput(attrs={'type': 'color', 'class': 'formColor'}))
    mainTextColor = forms.CharField(widget=forms.TextInput(attrs={'type': 'color', 'class': 'textColor'}))

    class Meta:
        model = JamColor
        fields = ['backgroundColor', 'formColor', 'mainTextColor']