from django.shortcuts import render, redirect
from django.views import View

from registration.forms import UserRegistrationForm, UserPhotoForm, UserDataForm
from registration.utils import UserFormSaver, GetRegisterFormContext


class UserRegistrationView(View):

    @staticmethod
    def get(request, **kwargs):
        if request.user.is_authenticated:
            return redirect('jamList')
        context = GetRegisterFormContext()
        return render(request, '../templates/user/registration.html', context=context)


    @staticmethod
    def post(request, **kwargs):
        form = UserRegistrationForm(request.POST)
        dataForm = UserDataForm(request.POST)
        photoForm = UserPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(True)
            UserFormSaver.UserPhotoSave(dataForm, user)
            UserFormSaver.UserDataSave(photoForm, user)
            UserFormSaver.SetUserRight(user, 1)
            return redirect('login')
        else:
            context = GetRegisterFormContext(form, dataForm, photoForm)
            return render(request, '../templates/user/registration.html', context=context)
