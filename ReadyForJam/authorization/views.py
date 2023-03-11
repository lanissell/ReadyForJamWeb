from django.shortcuts import render
from django.views import View

from authorization.form import UserRegistrationForm, UserLoginForm
from authorization.utils import CreateAuthorViewContext
from globalUtils import UploadFile


class UserLoginView(View):
    @staticmethod
    def get(request, **kwargs):
        context = CreateAuthorViewContext('Вход',
                                          'Войти',
                                          'Нет аккаунта',
                                          'register',
                                          UserLoginForm)
        return render(request, '../templates/user/authorization.html', context=context)


class UserRegistrationView(View):

    @staticmethod
    def get(request, **kwargs):
        context = CreateAuthorViewContext('Регистрация',
                                          'Зарегистрироваться',
                                          'Есть аккаунт',
                                          'login',
                                          UserRegistrationForm)
        return render(request, '../templates/user/authorization.html', context=context)

    @staticmethod
    def post(request, **kwargs):

        form = UserRegistrationForm(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            user = form.save(commit=True)
            context['user'] = user
        return render(request, '../templates/user/post-registration.html', context=context)

