from django.http import HttpResponse
from django.views import View


class UserProfileView(View):

    @staticmethod
    def get(request, **kwargs):
        if kwargs['uid'] != ' ':
            return HttpResponse('<h2>' + kwargs['uid'] + '</h2>')

