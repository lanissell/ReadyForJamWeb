from django import forms


class UserRegistrationForm(forms.Form):
    attrs = {'class': 'registration__item-input'}

    NickName = forms.CharField(label='Ник', widget=forms.TextInput(
        attrs=attrs
    ))
    Password = forms.CharField(min_length=8, label='Пароль', widget=forms.PasswordInput(
        attrs=attrs
    ))
    PasswordRepeat = forms.CharField(min_length=8, label='Повторите пароль', widget=forms.PasswordInput(
        attrs=attrs
    ))
    EMail = forms.CharField(label='E-Mail', widget=forms.EmailInput(
        attrs=attrs
    ))
    BirthDate = forms.DateField(label='Дата рождения', widget=forms.SelectDateWidget())
    About = forms.CharField(label='О себе', required=False, widget=forms.Textarea(
        attrs=attrs
    ))
    Photo = forms.ImageField(label='Аватар', required=False, widget=forms.FileInput(
        attrs={'class': 'registration__item-image'}
    ))


