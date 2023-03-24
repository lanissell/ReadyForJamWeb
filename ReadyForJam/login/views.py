from django.shortcuts import render
from django.views import View

from login.forms import UserLoginForm
from registration.utils import CreateFormViewContext


class UserLoginView(View):

    @staticmethod
    def get(request, **kwargs):
        context = CreateFormViewContext('Вход в аккаунт',
                                        '/login/',
                                        'Войти',
                                        UserLoginForm)
        context['changePageBtnText'] = 'Нет аккаунта'
        context['changePageBtnUrl'] = 'register'
        return render(request, '../templates/user/form-template.html', context=context)

    @staticmethod
    def post(request, **kwargs):
        return render(request, '../templates/user/post-registration.html')
