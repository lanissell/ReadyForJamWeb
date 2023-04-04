from django.urls import path, re_path

import jam.views as jv

urlpatterns = [
    path('register/', jv.JamRegistrationView.as_view(), name='jamRegister'),
    path('all/', jv.JamListView.as_view(), name='jamList'),
    re_path(r'^([\S\w]+)/?', jv.JamPageView.as_view(), name='jamPage'),
]
