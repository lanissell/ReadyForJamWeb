from django import forms


class UserLoginForm(forms.Form):
    attrs = {'class': 'registration__item-input'}

    Login = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs=attrs
    ))
    Password = forms.CharField(min_length=8, label='Пароль', widget=forms.PasswordInput(
        attrs=attrs
    ))


class UserRegistrationForm(UserLoginForm):
    PasswordRepeat = forms.CharField(min_length=8, label='Повторите пароль', widget=forms.PasswordInput(
        attrs=UserLoginForm.attrs
    ))
    EMail = forms.CharField(label='E-Mail', widget=forms.EmailInput(
        attrs=UserLoginForm.attrs
    ))
    BirthDate = forms.DateField(label='Дата рождения', widget=forms.SelectDateWidget())
    About = forms.CharField(label='О себе', required=False, widget=forms.Textarea(
        attrs=UserLoginForm.attrs
    ))
    Photo = forms.ImageField(label='Аватар', required=False, widget=forms.FileInput(
        attrs={'class': 'registration__item-image'}
    ))
