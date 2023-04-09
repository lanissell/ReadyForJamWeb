from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
import datetime

from globalUtils import BasicHtmlAttrs
from registration.models import UserPhoto, UserData

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class DateInput(forms.DateInput):
    input_type = 'date'


class UserRegistrationForm(UserCreationForm):
    attrs = BasicHtmlAttrs.inputFieldAttrs

    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs=attrs
    ), error_messages={'unique': 'Логин занят'})
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs=attrs
    ))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(
        attrs=attrs
    ))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(
        attrs=attrs
    ), error_messages={'invalid': 'Не корректно введена почта'})


    def clean(self):
        cleanedData = super().clean()
        password = cleanedData.get("password1")
        passwordRepeat = cleanedData.get("password2")
        if password != passwordRepeat:
            raise ValidationError("Пароли не совпадают")
        return cleanedData

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserDataForm(ModelForm):
    attrs = BasicHtmlAttrs.inputFieldAttrs
    dateAttrs = {
        'class': attrs['class'],
        'max': f"{datetime.datetime.now().year}-12-31",
        'min': "1900-12-31"
    }
    birthDate = forms.DateField(label='Дата рождения', widget=DateInput(
        attrs=dateAttrs
    ))
    about = forms.CharField(label='Немного о себе', widget=forms.Textarea(
        attrs={'class': 'registration__item-about-me'}
    ))
    class Meta:
        model = UserData
        fields = ['birthDate', 'about']

class UserPhotoForm(ModelForm):
    avatar = forms.ImageField(label='Аватар', widget=forms.FileInput(
        attrs=BasicHtmlAttrs.attrs
    ))

    class Meta:
        model = UserPhoto
        fields = ['avatar']
