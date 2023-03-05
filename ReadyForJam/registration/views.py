from django.shortcuts import render
from django.views import View

from registration.form import UserRegistrationForm
from globalUtils.utils import HandleUploadedFile


class UserRegistrationView(View):

    @staticmethod
    def get(request, **kwargs):
        return render(request, '../templates/user/registration.html', {'form': UserRegistrationForm})

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
        return render(request, '../templates/user/registration.html', context=context)
