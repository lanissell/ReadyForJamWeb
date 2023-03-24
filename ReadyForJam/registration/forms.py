from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
import datetime

from registration.utils import BasicHtmlAttrs
from registration.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class UserRegistrationForm(ModelForm):
    attrs = BasicHtmlAttrs.inputFieldAttrs

    login = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs=attrs
    ))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs=attrs
    ))
    passwordRepeat = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(
        attrs=attrs
    ))
    email = forms.CharField(label='E-mail', widget=forms.EmailInput(
        attrs=attrs
    ))
    about = forms.CharField(label='Немного о себе', widget=forms.Textarea(
        attrs={'class': 'registration__item-about-me'}
    ))

    dateAttrs = {
        'class': attrs['class'],
        'max': f"{datetime.datetime.now().year}-12-31",
        'min': "1900-12-31"
    }

    birthDate = forms.DateField(label='Дата рождения', widget=DateInput(
        attrs=dateAttrs
    ))

    class Meta:
        model = User
        fields = ['login', 'password', 'email', 'about', 'birthDate']

    def clean_passwordRepeat(self):
        password = self.cleaned_data['password']
        passwordRepeat = self.cleaned_data['passwordRepeat']
        if password != passwordRepeat:
            raise ValidationError('Пароли не совпадают')
        return passwordRepeat

    field_order = ['login', 'password', 'passwordRepeat', 'email', 'birthDate', 'about']
