from django.shortcuts import render
from django.views import View

from jam.forms import JamRegistrationForm


class JamRegistrationView(View):

    @staticmethod
    def get(request, **kwargs):
        context = {}
        return render(request, '../templates/jam/form-template.html', context=context)

    @staticmethod
    def post(request, **kwargs):
        return render(request, '../templates/user/post-registration.html')