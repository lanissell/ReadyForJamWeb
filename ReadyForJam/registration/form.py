from django import forms


class UserRegistrationForm(forms.Form):
    NickName = forms.CharField(label='Ник')
    Password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Пароль')
    PasswordRepeat = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторите пароль')
    EMail = forms.CharField(widget=forms.EmailInput, label='E-Mail')
    BirthDate = forms.DateField(widget=forms.SelectDateWidget, label='Дата рождения')
    About = forms.CharField(widget=forms.Textarea(), label='О себе', required=False)
    Photo = forms.ImageField(label='Аватар', required=False)


