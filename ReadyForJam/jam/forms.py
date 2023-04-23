from datetime import datetime

from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, modelformset_factory
from django import forms

from jam.models import Jam, JamColor, JamDate, JamCriteria
from globalUtils import BasicHtmlAttrs


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
    content = forms.Field(label='Содержание страницы',
                              widget=CKEditorWidget())

    class Meta:
        model = Jam
        fields = ['name', 'theme', 'avatar', 'content']

    field_order = ['name', 'theme', 'avatar']


class DateInput(forms.DateInput):
    input_type = 'datetime-local'


class JamDateForm(ModelForm):
    dateAttrs = {
        'class': "registration__date-input",
        'max': f"{datetime.now().year + 20}-12-31",
        'min': "1900-12-31"
    }

    startDate = forms.CharField(label='Начало джема', widget=DateInput(
        attrs=dateAttrs
    ))
    votingStartDate = forms.CharField(label='Начало голосования', widget=DateInput(
        attrs=dateAttrs
    ))
    votingEndDate = forms.CharField(label='Конец голосования', widget=DateInput(
        attrs=dateAttrs
    ))

    class Meta:
        model = JamDate
        fields = ['startDate', 'votingStartDate', 'votingEndDate']


class JamColorForm(ModelForm):
    colorAttrs = {'type': 'color', 'value': '#525252', 'class':'registration__color-input'}

    backgroundColor = forms.CharField(label='Цвет фона', widget=forms.TextInput(
        attrs=colorAttrs
    ))
    mainTextColor = forms.CharField(label='Основной цвет текста', widget=forms.TextInput(
        attrs=colorAttrs
    ))
    colorAttrs['id'] = 'formColor'
    formColor = forms.CharField(label='Цвет формы', widget=forms.TextInput(
        attrs=colorAttrs
    ))

    class Meta:
        model = JamColor
        fields = ['backgroundColor', 'formColor', 'mainTextColor']

class JamCriteriaForm(ModelForm):

    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'criteria-block__input'}
    ))
    class Meta:
        model = JamCriteria
        fields = ['name']

JamCriteriaFormSet = modelformset_factory(JamCriteria,
                                          form=JamCriteriaForm,
                                          extra=1)