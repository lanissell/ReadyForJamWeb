from django import forms

from registration.utils import BasicHtmlAttrs


class UserLoginForm(forms.Form):

    login = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs=BasicHtmlAttrs.inputFieldAttrs
    ))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs=BasicHtmlAttrs.inputFieldAttrs
    ))

