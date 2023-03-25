from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from registration.forms import UserRegistrationForm, UserPhotoForm
from registration.models import User
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
        context['photoForm'] = UserPhotoForm
        return render(request, '../templates/user/form-template.html', context=context)


    @staticmethod
    def post(request, **kwargs):
        form = UserRegistrationForm(request.POST)
        context = {}
        if form.is_valid():
            user = form.save(commit=True)
            if user.id is not None:
                photoForm = UserPhotoForm(request.POST, request.FILES)
                if photoForm.is_valid():
                    photo = photoForm.save(commit=False)
                    photo.user = User.objects.get(pk=user.id)
                    photo.save()
                    context['userPhoto'] = photo
            context['user'] = user
            return render(request, '../templates/user/post-registration.html', context=context)
        else:
            for m in form.errors.values():
                messages.error(request, m)
            return redirect('registration')
