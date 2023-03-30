from django.urls import path, re_path

import jam.views

urlpatterns = [
    path('register/', jam.views.JamRegistrationView.as_view(), name='jamRegister'),
    re_path(r'^([\S\w]+)/?', jam.views.JamPageView.as_view(), name='jamPage'),
]
