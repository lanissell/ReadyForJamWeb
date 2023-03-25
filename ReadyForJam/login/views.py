from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View

from login.forms import UserLoginForm
from registration.models import User, UserPhoto


class UserLoginView(View):

    @staticmethod
    def get(request, **kwargs):
        context = {'form': UserLoginForm}
        return render(request, '../templates/user/login.html', context=context)

    @staticmethod
    def post(request, **kwargs):
        isValid = True
        form = UserLoginForm(request.POST)
        login = form['login'].value()
        password = form['password'].value()
        try:
            user = User.objects.get(login=login)
        except ObjectDoesNotExist:
            user = None
        if user is None:
            messages.error(request, 'Пользователь не найден')
            isValid = False
        elif not check_password(password, user.password):
            messages.error(request, 'Не верный пароль')
            isValid = False
        if isValid:
            context = {'user': user}
            try:
                userPhoto = UserPhoto.objects.get(user = user)
                context['userPhoto'] = userPhoto
            except ObjectDoesNotExist:
                print('Photo not found')
            return render(request, '../templates/user/post-registration.html', context)
        return redirect('login')

