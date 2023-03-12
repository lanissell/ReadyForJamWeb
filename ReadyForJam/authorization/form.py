from django.forms import ModelForm
from django import forms


from user.models import User


class UserLoginForm(ModelForm):
    class Meta:
        attrs = {'class': 'registration__item-input'}
        model = User
        fields = ['NickName', 'Password']
        widgets = {
            'NickName': forms.TextInput(attrs=attrs),
            'Password': forms.PasswordInput(attrs=attrs),
        }
        labels = {
            'NickName': 'Ник',
            'Password': 'Пароль',
        }


class UserRegistrationForm(UserLoginForm):
    PasswordRepeat = forms.CharField(min_length=8, label='Повторите пароль', widget=forms.PasswordInput(
        attrs=UserLoginForm.Meta.attrs
    ))
    EMail = forms.CharField(label='E-Mail', widget=forms.EmailInput(
        attrs=UserLoginForm.Meta.attrs
    ))

    BirthDate = forms.DateField(label='Дата рождения', widget=forms.SelectDateWidget())
    About = forms.CharField(label='О себе', required=False, widget=forms.Textarea(
        attrs={'class': 'registration__item-about-me '}
    ))

    class Meta(UserLoginForm.Meta):
        fieldName = 'AvatarUrl'
        parentMeta = UserLoginForm.Meta
        parentMeta.fields.append(fieldName)
        parentMeta.labels[fieldName] = 'Аватар'
        parentMeta.widgets[fieldName] = forms.FileInput

    field_order = ['NickName', 'Password', 'PasswordRepeat', 'EMail', 'BirthDate', 'About', 'AvatarUrl']
