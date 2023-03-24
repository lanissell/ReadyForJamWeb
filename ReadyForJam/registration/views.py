from django.shortcuts import render
from django.views import View

from registration.forms import UserRegistrationForm
from registration.utils import CreateFormViewContext


class UserRegistrationView(View):

    @staticmethod
    def get(request, **kwargs):
        context = CreateFormViewContext('Регистрация',
                                        '/register/',
                                        'Зарегистрироваться',
                                        UserRegistrationForm)
        context['changePageBtnText'] = 'Есть аккаунт'
        context['changePageBtnUrl'] = 'login'
        return render(request, '../templates/user/form-template.html', context=context)

    @staticmethod
    def post(request, **kwargs):
        form = UserRegistrationForm(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            user = form.save(commit=True)
            context['user'] = user
            return render(request, '../templates/user/post-registration.html', context=context)
        return render(request, '../templates/user/post-registration.html', context=context)
