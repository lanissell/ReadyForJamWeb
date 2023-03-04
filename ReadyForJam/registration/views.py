from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from registration.form import UserRegistrationForm
from registration.utils import handle_uploaded_file


class UserRegistrationView(View):

    @staticmethod
    def get(request, **kwargs):
        return render(request, '../templates/Registartion.html', {'form': UserRegistrationForm})

    @staticmethod
    def post(request, **kwargs):
        NickName = request.POST.get("NickName")
        path = handle_uploaded_file(request.FILES['Image'],
                                    request.FILES['Image'].name)
        context = {
            'Nick': NickName,
            'Photo': '/' + path
        }
        return render(request, '../templates/Registartion.html', context=context)
