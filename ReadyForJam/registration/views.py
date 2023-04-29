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
        return render(request, '/user/registration.html', context=context)


    @staticmethod
    def post(request, **kwargs):
        form = UserRegistrationForm(request.POST)
        dataForm = UserDataForm(request.POST)
        photoForm = UserPhotoForm(request.POST, request.FILES)

        formSaver = UserFormSaver()
        formSaver.MainFormSave(form)
        formSaver.RelativeFormSave(dataForm)
        formSaver.RelativeFormSave(photoForm)
        formSaver.SetCurrentUserRight(1)

        if formSaver.isFormsValidated:
            return redirect('login')
        else:
            context = GetRegisterFormContext(form, dataForm, photoForm)
            return render(request, '../templates/user/registration.html', context=context)
