from django.shortcuts import render
from django.views import View

from authorization.form import UserRegistrationForm, UserLoginForm
from authorization.utils import CreateAuthorViewContext
from globalUtils import HandleUploadedFile


class UserLoginView(View):
    @staticmethod
    def get(request, **kwargs):
        context = CreateAuthorViewContext('Вход',
                                          'Войти',
                                          'Нет аккаунта',
                                          'register',
                                          UserLoginForm)
        return render(request, '../templates/user/user-registration.html', context=context)


class UserRegistrationView(View):

    @staticmethod
    def get(request, **kwargs):
        context = CreateAuthorViewContext('Регистрация',
                                          'Зарегистрироваться',
                                          'Есть аккаунт',
                                          'login',
                                          UserRegistrationForm)
        return render(request, '../templates/user/user-registration.html', context=context)

    @staticmethod
    def post(request, **kwargs):
        nickName = request.POST.get("NickName")
        eMail = request.POST.get("EMail")
        path = HandleUploadedFile(request.FILES['Photo'],
                                  'static/user/img/',
                                  request.FILES['Photo'].name)
        context = {
            'nick': nickName,
            'eMail': eMail,
            'photo': '/' + path,
        }
        return render(request, '../templates/user/post-registration.html', context=context)

