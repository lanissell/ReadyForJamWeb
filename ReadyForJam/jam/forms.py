from datetime import datetime

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.forms import ModelForm
from django import forms

from jam.models import Jam, JamColor, JamDate
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
    avatar = forms.ImageField(label='Аватар', widget=forms.FileInput(
        attrs=attrs
    ))
    content = forms.CharField(label='Содержание страницы',
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = Jam
        fields = ['name', 'theme', 'avatar', 'content']

    field_order = ['name', 'theme', 'avatar']


class DateInput(forms.DateInput):
    input_type = 'datetime-local'


class JamDateForm(ModelForm):
    dateAttrs = {
        'class': BasicHtmlAttrs.inputFieldAttrs['class'],
        'max': f"{datetime.now().year + 20}-12-31",
        'min': "1900-12-31"
    }

    startDate = forms.DateTimeField(label='Дата начала джема', widget=DateInput(
        attrs=dateAttrs
    ))
    votingStartDate = forms.DateTimeField(label='Дата начала голосования', widget=DateInput(
        attrs=dateAttrs
    ))
    votingEndDate = forms.DateTimeField(label='Дата окончания голосования', widget=DateInput(
        attrs=dateAttrs
    ))

    class Meta:
        model = JamDate
        fields = ['startDate', 'votingStartDate', 'votingEndDate']


class JamColorForm(ModelForm):
    colorAttrs = {'type': 'color', 'value': '#525252'}

    backgroundColor = forms.CharField(label='Цвет фона', widget=forms.TextInput(
        attrs={'type': colorAttrs['type'], 'value': colorAttrs['value'], 'class': 'bgColor', }
    ))
    formColor = forms.CharField(label='Цвет формы', widget=forms.TextInput(
        attrs={'type': colorAttrs['type'], 'value': colorAttrs['value'], 'class': 'formColor', }
    ))
    mainTextColor = forms.CharField(label='Основной цвет текста', widget=forms.TextInput(
        attrs={'type': colorAttrs['type'], 'value': colorAttrs['value'], 'class': 'textColor'}
    ))

    class Meta:
        model = JamColor
        fields = ['backgroundColor', 'formColor', 'mainTextColor']
