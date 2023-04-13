from django.urls import path, re_path

import jam.views as jv

urlpatterns = [
    path('register/', jv.JamRegistrationView.as_view(), name='jamRegister'),
    path('all/', jv.JamListView.as_view(), name='jamList'),
    path('<str:jamName>', jv.JamPageView.as_view(), name='jamPage'),
    path('<str:jamName>/update', jv.JamUpdateView.as_view(), name='jamUpdate'),
]
