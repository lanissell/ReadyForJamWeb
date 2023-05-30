from django import forms
from django.contrib.auth.forms import AuthenticationForm

from globalUtils import BasicHtmlAttrs


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs=BasicHtmlAttrs.inputFieldAttrs
    ))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs=BasicHtmlAttrs.inputFieldAttrs
    ))

    error_messages = {
        'invalid_login': 'Не верный логин или пароль'
    }

