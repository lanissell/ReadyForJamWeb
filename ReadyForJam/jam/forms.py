from datetime import datetime

from django.forms import ModelForm, modelformset_factory
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

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

    class Meta:
        model = Jam
        fields = ['name', 'theme', 'avatar', 'content']
        widgets = {
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }

    field_order = ['name', 'theme', 'avatar', 'content']


class DateInput(forms.DateInput):
    input_type = 'datetime-local'


class JamDateForm(ModelForm):
    dateAttrs = {
        'class': "registration__date-input",
        'max': f"{datetime.now().year + 20}-12-31",
        'min': "1900-12-31"
    }

    start_date = forms.CharField(label='Начало джема', widget=DateInput(
        attrs=dateAttrs
    ))
    voting_start_date = forms.CharField(label='Начало голосования', widget=DateInput(
        attrs=dateAttrs
    ))
    voting_end_date = forms.CharField(label='Конец голосования', widget=DateInput(
        attrs=dateAttrs
    ))

    class Meta:
        model = JamDate
        fields = ['start_date', 'voting_start_date', 'voting_end_date']


class JamColorForm(ModelForm):
    colorAttrs = BasicHtmlAttrs.colorFieldAttrs

    background_color = forms.CharField(label='Цвет фона', widget=forms.TextInput(
        attrs=colorAttrs
    ))
    main_text_color = forms.CharField(label='Основной цвет текста', widget=forms.TextInput(
        attrs=colorAttrs
    ))
    colorAttrs['id'] = 'formColor'
    form_color = forms.CharField(label='Цвет формы', widget=forms.TextInput(
        attrs=colorAttrs
    ))

    class Meta:
        model = JamColor
        fields = ['background_color', 'form_color', 'main_text_color']

class JamCriteriaForm(ModelForm):

    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'criteria-block__input'}
    ))
    class Meta:
        model = JamCriteria
        fields = ['name']

JamCriteriaFormSet = modelformset_factory(JamCriteria,
                                          form=JamCriteriaForm,
                                          can_order=False,
                                          extra=1)

