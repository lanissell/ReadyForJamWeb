from django.urls import path

import jam.views

urlpatterns = [
    path('register/', jam.views.JamRegistrationView.as_view(), name='jamRegister'),
]
