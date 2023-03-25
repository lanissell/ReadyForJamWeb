from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View

from registration.forms import UserRegistrationForm, UserPhotoForm
from registration.models import User, UserRight, Right


def UserPhotoSave(request, userObject):
    photoForm = UserPhotoForm(request.POST, request.FILES)
    photo = None
    if photoForm.is_valid():
        photo = photoForm.save(commit=False)
        photo.user = userObject
        photo.save()
    return photo

def SetUserRight(userObject, rightId):
    userRight = UserRight()
    userRight.user = userObject
    right = Right.objects.get(pk=rightId)
    userRight.right = right
    userRight.save()


class UserRegistrationView(View):

    @staticmethod
    def get(request, **kwargs):
        context = {'form': UserRegistrationForm, 'photoForm': UserPhotoForm}
        return render(request, '../templates/user/registration.html', context=context)


    @staticmethod
    def post(request, **kwargs):
        form = UserRegistrationForm(request.POST)
        context = {}
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            if user.id is not None:
                userObject = User.objects.get(pk=user.id)
                photo = UserPhotoSave(request, userObject)
                if photo:
                    context['userPhoto'] = photo
                SetUserRight(userObject, 1)
                context['user'] = user
            return render(request, '../templates/user/post-registration.html', context=context)
        else:
            for m in form.errors.values():
                messages.error(request, m)
            return redirect('registration')
