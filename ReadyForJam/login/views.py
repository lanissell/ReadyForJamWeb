from django.shortcuts import render
from django.views import View

from login.form import UserLoginForm
from registration.utils import CreateAuthorViewContext


class UserLoginView(View):

    @staticmethod
    def get(request, **kwargs):
        context = CreateAuthorViewContext('Вход в аккаунт',
                                          'Войти',
                                          'Нет аккаунта',
                                          'register',
                                          UserLoginForm)
        return render(request, '../templates/user/form-template.html', context=context)

    @staticmethod
    def post(request, **kwargs):
        return render(request, '../templates/user/post-registration.html')
